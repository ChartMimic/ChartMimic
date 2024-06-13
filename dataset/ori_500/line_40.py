# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)


# ===================
# Part 2: Data Preparation
# ===================
# New generated data
snr_values = np.linspace(5, 25, 5)
jpeg_ldpc = np.random.normal(loc=50, scale=5, size=5).clip(10, 90)
deepjscc_wo_ofdm = np.random.normal(loc=40, scale=10, size=5).clip(5, 45)
deepjscc_w_ofdm = np.random.normal(loc=70, scale=10, size=5).clip(20, 95)
ours = np.random.normal(loc=85, scale=5, size=5).clip(30, 100)

# Labels and Plot Types
label_jpeg_ldpc = "JPEG+LDPC"
label_deepjscc_wo_ofdm = "DEEPJSCC w/o OFDM"
label_deepjscc_w_ofdm = "DEEPJSCC w/ OFDM"
label_ours = "OURS"

# Axes Limits and Labels
yticks_values = np.arange(0, 110, 10)
ylim_values = [0, 105]
xlabel_value = "SNR"
ylabel_value = "Classification Accuracy (%)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting with error bars (second-level element)
plt.figure(figsize=(8, 6))  # Increased figure size for clarity
plt.plot(snr_values, jpeg_ldpc, "-o", label=label_jpeg_ldpc, color="#1f77b4")
plt.fill_between(snr_values, jpeg_ldpc - 5, jpeg_ldpc + 5, color="#1f77b4", alpha=0.2)
plt.plot(snr_values, deepjscc_wo_ofdm, "-^", label=label_deepjscc_wo_ofdm, color="#ff7f0e")
plt.fill_between(
    snr_values, deepjscc_wo_ofdm - 10, deepjscc_wo_ofdm + 10, color="#ff7f0e", alpha=0.2
)
plt.plot(snr_values, deepjscc_w_ofdm, "-x", label=label_deepjscc_w_ofdm, color="#2ca02c")
plt.fill_between(
    snr_values, deepjscc_w_ofdm - 10, deepjscc_w_ofdm + 10, color="#2ca02c", alpha=0.2
)
plt.plot(snr_values, ours, "-s", label=label_ours, color="#d62728")
plt.fill_between(snr_values, ours - 5, ours + 5, color="#d62728", alpha=0.2)

# Customizing axes and labels (third-level elements)
plt.yticks(yticks_values, fontsize=12)
plt.xticks(fontsize=12)
plt.ylim(ylim_values)
plt.grid(True)

# Relocating the legend to ensure no overlap with data lines
plt.legend(loc="lower right", frameon=True, shadow=True, fontsize=10)

# Customizing the background (third-level element)
plt.gca().set_facecolor("#f4f4f5")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# Labels
plt.xlabel(xlabel_value, fontsize=14)
plt.ylabel(ylabel_value, fontsize=14)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('line_40.pdf', bbox_inches='tight')
