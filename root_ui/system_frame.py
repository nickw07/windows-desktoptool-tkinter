
import tkinter as tk
from tkinter import ttk

import wmi
import platform
import psutil


class SystemFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.ERROR = "Could not be read"
        self.INFO = "Press button for info"

        self.pc_name = tk.StringVar(value=self.INFO)
        self.pc_os = tk.StringVar(value=self.INFO)

        self.pc_cpu = tk.StringVar(value=self.INFO)
        self.pc_gpu = tk.StringVar(value=self.INFO)

        self.pc_ram = tk.StringVar(value=self.INFO)
        self.pc_drive = tk.StringVar(value=self.INFO)

        # frame description
        frame_description_label = ttk.Label(self,
                                            text="Your System",
                                            style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=240, y=12)

        self.load_info_button_icon = tk.PhotoImage(file=r"graphics/system-frame/load-32x32px.png")
        load_info_button = ttk.Button(self,
                                      image=self.load_info_button_icon,
                                      command=self.load_all,
                                      style="AppButton.TButton")
        load_info_button.place(x=365, y=4)

        self.pc_image = tk.PhotoImage(file=r"graphics/system-frame/laptop-image.png")
        pc_image = ttk.Label(self,
                             image=self.pc_image,
                             style="Image.TLabel")
        pc_image.place(x=15, y=50)

        # frame functionality - CPU-Info/Software-Info/Storage-Info
        # 1
        processing_units_info_heading = ttk.Label(self,
                                                  text="PROCESSING-UNIT INFORMATION:",
                                                  style="HardwareInfoHeading.TLabel")
        processing_units_info_heading.place(x=20, y=250)

        cpu_description_label = ttk.Label(self,
                                          text="CPU:",
                                          style="DescriptionLabelSmaller.TLabel")
        cpu_description_label.place(x=20, y=285)

        cpu_info_label = ttk.Label(self,
                                   textvariable=self.pc_cpu,
                                   style="HardwareComponentInfo.TLabel")
        cpu_info_label.place(x=67, y=285)

        gpu_description_label = ttk.Label(self,
                                          text="GPU:",
                                          style="DescriptionLabelSmaller.TLabel")
        gpu_description_label.place(x=20, y=315)

        gpu_info_label = ttk.Label(self,
                                   textvariable=self.pc_gpu,
                                   style="HardwareComponentInfo.TLabel")
        gpu_info_label.place(x=67, y=315)

        # 2
        software_info_heading = ttk.Label(self,
                                          text="SOFTWARE INFORMATION:",
                                          style="HardwareInfoHeading.TLabel")
        software_info_heading.place(x=335, y=70)

        name_description_label = ttk.Label(self,
                                           text="PC-NAME:",
                                           style="DescriptionLabelSmaller.TLabel")
        name_description_label.place(x=335, y=105)

        name_info_label = ttk.Label(self,
                                    textvariable=self.pc_name,
                                    style="HardwareComponentInfo.TLabel")
        name_info_label.place(x=422, y=105)

        os_description_label = ttk.Label(self,
                                         text="OS:",
                                         style="DescriptionLabelSmaller.TLabel")
        os_description_label.place(x=335, y=135)

        os_info_label = ttk.Label(self,
                                  textvariable=self.pc_os,
                                  style="HardwareComponentInfo.TLabel")
        os_info_label.place(x=370, y=135)

        # 3
        storage_info_heading = ttk.Label(self,
                                         text="STORAGE INFORMATION:",
                                         style="HardwareInfoHeading.TLabel")
        storage_info_heading.place(x=335, y=180)

        ram_description_label = ttk.Label(self,
                                          text="RAM:",
                                          style="DescriptionLabelSmaller.TLabel")
        ram_description_label.place(x=335, y=215)

        ram_info_label = ttk.Label(self,
                                   textvariable=self.pc_ram,
                                   style="HardwareComponentInfo.TLabel")
        ram_info_label.place(x=382, y=215)

        drive_description_label = ttk.Label(self,
                                            text="DRIVE:",
                                            style="DescriptionLabelSmaller.TLabel")
        drive_description_label.place(x=335, y=245)

        drive_info_label = ttk.Label(self,
                                     textvariable=self.pc_drive,
                                     style="HardwareComponentInfo.TLabel")
        drive_info_label.place(x=395, y=245)

    def load_general_info(self):
        # overall data collection
        pc = wmi.WMI()

        # specific utilization of the return values
        name_info = platform.node()
        self.pc_name.set(name_info)

        os_info = pc.Win32_OperatingSystem()[0].caption
        self.pc_os.set(os_info)

        cpu_info = pc.Win32_Processor()[0].name
        self.pc_cpu.set(cpu_info)

        gpu_info = pc.Win32_VideoController()[0].name
        self.pc_gpu.set(gpu_info)

    def load_storage_info(self):
        # ram information
        try:
            ram_total_size = str(round((psutil.virtual_memory().total / 1024 / 1024 / 1024), 2))
            ram_currently_using_size = str(round((psutil.virtual_memory().used / 1024 / 1024 / 1024), 2))

            ram_info = f"{ram_total_size}GB, using {ram_currently_using_size}GB"
            self.pc_ram.set(ram_info)

        except PermissionError:
            self.pc_ram.set(self.ERROR)

        # drive information
        try:
            first_partition = psutil.disk_partitions()[0]

            partition_usage = psutil.disk_usage(first_partition.mountpoint)

            drive_total_size = str(round((partition_usage.total / 1024 / 1024 / 1024), 2))
            drive_free_size = str(round((partition_usage.free / 1024 / 1024 / 1024), 2))

            drive_info = f"{drive_total_size}GB, {drive_free_size}GB free"
            self.pc_drive.set(drive_info)

        except PermissionError:
            self.pc_drive.set(self.ERROR)

    def load_all(self):
        try:
            # load all
            self.load_general_info()
            self.load_storage_info()
        except Exception as E:
            print(f"{E} - Information could not be read")
            self.pc_name.set(self.ERROR)
            self.pc_os.set(self.ERROR)
            self.pc_cpu.set(self.ERROR)
            self.pc_gpu.set(self.ERROR)
            self.pc_ram.set(self.ERROR)
            self.pc_drive.set(self.ERROR)