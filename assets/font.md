# Font File Download
For Times New Roman font:https://github.com/justrajdeep/fonts/blob/master/Times%20New%20Roman.ttf

For Arial font: https://github.com/justrajdeep/fonts/blob/master/Arial.ttf

# Add Font File to Matplotlib
1. Get the font directory of matplotlib
```python
import matplotlib 
matplotlib.matplotlib_fname()

#Expected Output:
/home/user1/miniconda3/envs/seisbench/lib/python3.11/site-packages/matplotlib/mpl-data/matplotlibrc
```
The font directory is `/home/user1/miniconda3/envs/seisbench/lib/python3.11/site-packages/matplotlib/mpl-data/fonts/ttf/`

2. Copy the downloaded font files to the font directory of matplotlib


3. Clear the font cache to make the new font available
```python
import matplotlib.font_manager
matplotlib.get_cachedir()
#Expected Output:
/home/user1/.cache/matplotlib
```

```bash
rm -rf /home/user1/.cache/matplotlib
```

4. Restart the kernel and check if the new font is available
```python
import matplotlib.pyplot as plt 
plt.rcParams["font.sans-serif"] = "Arial"

fig, ax = plt.subplots(figsize=(16/2,9/2), facecolor="#0c0c0c")
ax.axis("off")

fig.text(0.5,0.5, "xxxxxxxxxxxxxxxxxxx", ha = "center", va="center",
          size=50, fontweight='extra bold',color="white")
plt.show()
```