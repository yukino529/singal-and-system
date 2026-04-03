import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 

# --- 信号参数 ---
f_signal = 2 # 信号频率 2 Hz
Fs = 10      # 采样频率 10 Hz

# --- 连续信号数据 ---
t_continuous = np.linspace(0, 2, 1000) 
y_continuous = np.cos(2 * np.pi * f_signal * t_continuous)

# --- 离散信号数据 ---
t_discrete = np.arange(0, 2.01, 1/Fs)
y_discrete = np.cos(2 * np.pi * f_signal * t_discrete)

# --- 开始绘图 ---
# 创建一个包含2个子图的窗口，2行1列
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# 在第一个子图 (ax1) 上画连续信号
ax1.plot(t_continuous, y_continuous)
ax1.set_title("连续余弦信号")
ax1.set_xlabel("时间 (t) / 秒")
ax1.set_ylabel("幅值")
ax1.grid(True)

# 在第二个子图 (ax2) 上画离散信号

ax2.stem(t_discrete, y_discrete)
ax2.set_title(f"采样后的离散余弦信号 (Fs = {Fs} Hz)")
ax2.set_xlabel("时间 (t) / 秒")
ax2.set_ylabel("幅值")
ax2.grid(True)

# 调整子图之间的间距，防止标题重叠
plt.tight_layout()

# 只需要在最后调用一次 show()
plt.show()