import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from tqdm import tqdm_notebook

# 頂点データを取り出す。
df_obj_v = pd.read_csv('bunny.obj', sep=' ', header=None)
df_obj_v.columns = ['data', 'x', 'y', 'z', 'r', 'g', 'b']
df_obj_v = df_obj_v[df_obj_v['data'] == 'v']
df_obj_v = df_obj_v[['x', 'y', 'z', 'r', 'g', 'b']].astype(np.float64)

# 面データを取り出す。(実は使ってない)
df_obj_f = pd.read_csv('bunny.obj', sep=' ', header=None, usecols=[0,1,2,3])
df_obj_f.columns = ['data', 'v1', 'v2', 'v3']
df_obj_f = df_obj_f[df_obj_f['data'] == 'f']
df_obj_f = df_obj_f[['v1', 'v2', 'v3']].astype(np.int)
df_obj_f = df_obj_f.reset_index(drop=True)

# zが低い点を消す。
df_obj_v_u = df_obj_v[df_obj_v.z > 40]

for i in tqdm_notebook(range(120)):
    e = 30
    azim = 90 + 3 * i

    fig = plt.figure(dpi=100)
    ax = Axes3D(fig, aspect='equal')

    ax.scatter(df_obj_v_u['x'], df_obj_v_u['y'], df_obj_v_u['z'], s=0.5, facecolors=df_obj_v_u[['r', 'g', 'b']])
    ax.view_init(elev = e, azim=azim)
    # 数字を0詰めにしないとImageMagickがうまく行かない。
    plt.savefig('for_gif_dot/{}.png'.format(str(i).zfill(3)), bbox_inches='tight')
    plt.close()