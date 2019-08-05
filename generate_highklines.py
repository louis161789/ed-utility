import numpy as np

# reciprocal lattice vectors in cartesian coordinations in 2pi/a unit where a: lattice constant
rec_vec = np.array([[-1.000000,-1.000000,1.000000],
                    [1.000000,1.000000,1.000000],
		    [-1.000000,1.000000,-1.000000]])

# high symmetry k point in crystal coordinates
G = np.array([0.000000,0.000000,0.000000])
X = np.array([0.000000,0.500000,0.500000])
W = np.array([0.250000,0.750000,0.500000])
L = np.array([0.500000,0.500000,0.500000])
K = np.array([0.375000,0.750000,0.375000])

step = 0.05

#################################################################################################
def num_pts_along_line(pt1,pt2,rec_vec,step):
    pt1_cart = pt1[0]*rec_vec[0]+pt1[1]*rec_vec[1]+pt1[2]*rec_vec[2]
    pt2_cart = pt2[0]*rec_vec[0]+pt2[1]*rec_vec[1]+pt2[2]*rec_vec[2]
    distance = np.linalg.norm(pt2_cart-pt1_cart)
    npts = int(distance/step)
    return npts

def point_along_line(pt1,pt2,npts):
# generate points between pt1 and pt2, including pt1 but not pt2
    x = np.linspace(pt1[0],pt2[0],npts,endpoint=False)
    y = np.linspace(pt1[1],pt2[1],npts,endpoint=False)
    z = np.linspace(pt1[2],pt2[2],npts,endpoint=False)
    x = x[:,np.newaxis]
    y = y[:,np.newaxis]
    z = z[:,np.newaxis]
    pt = np.concatenate((x,y,z),axis=1)
    return pt

def print_out_xk(pt):
# print out k points 
    for i in range(len(pt)):
        print "{:10.6f}   {:10.6f}   {:10.6f}".format(pt[i][0],pt[i][1],pt[i][2])

def print_out_xk_nscf(pt,ratio):
# print out k points for nscf calculations:
    for i in range(len(pt)):
        print "{:10.6f}   {:10.6f}   {:10.6f}  {:8.6f}".format(pt[i][0],pt[i][1],pt[i][2],ratio)
#################################################################################################

first_point = point_along_line(G,G,1)
#
npts_GX = num_pts_along_line(G,X,rec_vec,step)
points_GX = point_along_line(G,X,npts_GX)
#
npts_XW = num_pts_along_line(X,W,rec_vec,step)
points_XW = point_along_line(X,W,npts_XW)
#
npts_WL = num_pts_along_line(W,L,rec_vec,step)
points_WL = point_along_line(W,L,npts_WL)
#
npts_LG = num_pts_along_line(L,G,rec_vec,step)
points_LG = point_along_line(L,G,npts_LG)
#
npts_GK = num_pts_along_line(G,K,rec_vec,step)
points_GK = point_along_line(G,K,npts_GK)
#
npts_KX = num_pts_along_line(K,X,rec_vec,step)
points_KX = point_along_line(K,X,npts_KX)
#
last_point = point_along_line(X,X,1)

# the first point is the initial state
# the rest points are the final states
npts = 1 + npts_GX + npts_XW + npts_WL + npts_LG + npts_GK + npts_KX + 1
ratio = 1.0/npts

#print npts_GX
#print npts_GX + npts_XW
#print npts_GX + npts_XW + npts_WL
#print npts_GX + npts_XW + npts_WL + npts_LG
#print npts_GX + npts_XW + npts_WL + npts_LG + npts_GK
#print npts_GX + npts_XW + npts_WL + npts_LG + npts_GK + npts_KX

## k point along high symmetry lines
#print npts
#print_out_xk(first_point)
#print_out_xk(points_GX)
#print_out_xk(points_XW)
#print_out_xk(points_WL)
#print_out_xk(points_LG)
#print_out_xk(points_GK)
#print_out_xk(points_KX)
#print_out_xk(last_point)

## for nscf calculations
#print npts
#print_out_xk_nscf(first_point,ratio)
#print_out_xk_nscf(points_GX,ratio)
#print_out_xk_nscf(points_XW,ratio)
#print_out_xk_nscf(points_WL,ratio)
#print_out_xk_nscf(points_LG,ratio)
#print_out_xk_nscf(points_GK,ratio)
#print_out_xk_nscf(points_KX,ratio)
#print_out_xk_nscf(last_point,ratio)

