import numpy as np

def transform_coordinates(pos):
    # takes np.array of (n,3) as xyz
    pos2 = np.zeros_like(pos)
    for i in range(3):
        pos2[:,i] = pos[:,i] - pos[0,i]
    v01 = pos2[1,:]
    v02 = pos2[2,:]

    uv01 = v01/np.linalg.norm(v01)
    uv02 = v02/np.linalg.norm(v02)
    cos_12 =  np.dot(uv01,uv02)

    v_i = v01/np.linalg.norm(v01)
    v_j = uv02/cos_12 - uv01
    v_j = v_j/np.linalg.norm(v_j)
    v_k = np.cross(v_i,v_j)

    r = np.zeros((3,3))
    r[:,0] = v_i
    r[:,1] = v_j
    r[:,2] = v_k
    return np.dot(np.linalg.pinv(r),pos2.T).T

if __name__ == "__main__":
    from matplotlib import pyplot
    from mpl_toolkits.mplot3d import Axes3D
    from pylab import figure

    m = np.random.random((4,3))
    fig = figure()
    ax = Axes3D(fig)

    for i in range(len(m)):  #plot each point + it's index as text above
        ax.scatter(m[i,0],m[i,1],m[i,2],color='b')
        ax.text(m[i,0],m[i,1],m[i,2],'%s' % (str(i)),size=20,zorder=1,
                color='k')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    pyplot.show()

    m_norm = transform_coordinates(m)
    fig = figure()
    ax = Axes3D(fig)

    for i in range(len(m_norm)):  #plot each point + it's index as text above
        ax.scatter(m_norm[i,0],m_norm[i,1],m_norm[i,2],color='b')
        ax.text(m_norm[i,0],m_norm[i,1],m_norm[i,2],'%s' % (str(i)),size=20,zorder=1,
                color='k')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    pyplot.show()