from nvitop import Device
import datetime

def get_gpu_info():
    devices = Device.all()  # or Device.cuda.all()
    info_lines = []
    for device in devices:
        processes = device.processes()  # type: Dict[int, GpuProcess]
        sorted_pids = sorted(processes)

        info_lines.append(f"Device: {device}")
        info_lines.append(f"  - Fan speed:       {device.fan_speed()}%")
        info_lines.append(f"  - Temperature:     {device.temperature()}C")
        info_lines.append(f"  - GPU utilization: {device.gpu_utilization()}%")
        info_lines.append(f"  - Total memory:    {device.memory_total_human()}")
        info_lines.append(f"  - Used memory:     {device.memory_used_human()}")
        info_lines.append(f"  - Free memory:     {device.memory_free_human()}")
        info_lines.append(f"  - Processes ({len(processes)}): {sorted_pids}")
        for pid in sorted_pids:
            info_lines.append(f"    - {processes[pid]}")
        info_lines.append('-' * 120)
    return "\n".join(info_lines)

def save_gpu_info(filename):
    info = get_gpu_info()
    with open(filename, 'a') as f:
        f.write(f"\n{datetime.datetime.now()}\n")
        f.write(info)

if __name__ == "__main__":
    filename = "gpu_info.log"
    save_gpu_info(filename)
