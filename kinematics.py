#!/usr/bin/env python3

import numpy as np

l1 = 0.3
l2 = 0.3
h = 0.4


def direct_kinematic(q=None):
    t1, t2, t4, d3 = q
    if t1 > 2.5 or t1 < -2.5 or t2 > 2 or t2 < -2 or t4 > 3 or t4 < -3 or d3 < 0 or d3 > 0.45:
        raise Exception('ERROR Invalid Kinematics Params')

    Tb0 = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, h], [0, 0, 0, 1]])

    A01 = np.matrix([[np.cos(t1), -np.sin(t1), 0, l1*np.cos(t1)],
                     [np.sin(t1), np.cos(t1), 0, l1*np.sin(t1)],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

    A12 = np.matrix([[np.cos(t2), -np.sin(t2), 0, l2*np.cos(t2)],
                     [np.sin(t2), np.cos(t2), 0, l2*np.sin(t2)],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

    A23 = np.matrix([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, -d3],
                     [0, 0, 0, 1]])

    A34 = np.matrix([[np.cos(t4), -np.sin(t4), 0, 0],
                     [np.sin(t4), np.cos(t4), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

    Tbe = Tb0 * A01 * A12 * A23 * A34

    return Tbe


def inverse_kinematic(x, y, z):
    i = np.sqrt(x**2+y**2)
    t1 = np.arctan2(y, x) + np.arccos((l1**2 + i**2 - l2**2)/(2*l1*i))
    t2 = - (np.pi - np.arccos((l1**2 + l2**2 - i**2)/(2*l1*l2)))
    d3 = h - z
    if t1 > 2.5 or t1 < -2.5 or t2 > 2 or t2 < -2 or d3 < 0 or d3 > 0.45:
        raise Exception('ERROR Invalid Kinematics Params')
    return t1, t2, 0, d3  # returns t1, t2, t4=0, d3
    # t4 is always 0 because we are ignoring the gripper orientation


if __name__ == "__main__":
    while True:
        print("Please take a choice:")
        print("\t* i -> inverse kinematic")
        print("\t* d -> direct kinematic")
        print("\t* q -> quit")

        c = input(">> ")

        if c == 'q':
            break
        elif c == 'i':
            x, y, z = eval(
                input("Please insert the position to reach (x, y, z): "))
            try:
                t1, t2, t4, d3 = inverse_kinematic(x, y, z)
            except Exception as e:
                print(e)
                continue
            print("Joint 1: {:.3f} rad\nJoint 2: {:.2f} rad".format(t1, t2))
            print("Joint 3: {:.3f} m\nJoint 4: {:.2f} rad".format(d3, t4))
            print()
        elif c == 'd':
            t1, t2, t4, d3 = eval(
                input("Please insert the joints variable (t1, t2, t4, d3): "))
            try:
                pose = direct_kinematic((t1, t2, t4, d3))
            except Exception as e:
                print(e)
                continue
            print("The obtained pose is: ")
            np.set_printoptions(precision=3, suppress=True)
            print(pose)
            print()
        else:
            print("Invalid choice.")
