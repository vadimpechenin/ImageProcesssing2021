import numpy as np
import scipy.io

class LoadMatFile:
    @staticmethod
    def loadMatTrain(path_file, name_file1, name_file2):
        train_load_mat = scipy.io.loadmat(path_file + name_file1 + '.mat')
        test_load_mat = scipy.io.loadmat(path_file + name_file2 + '.mat')
        x_train1 = np.array(train_load_mat['x_train'])
        y_train1 = np.array(test_load_mat['y_train'])

        x_test1 = np.array(test_load_mat['x_test'])
        y_test1 = np.array(test_load_mat['y_test'])

        N = np.array(test_load_mat['N'])
        N_test = np.array(test_load_mat['N_test'])
        H = np.array(test_load_mat['H'])
        L = np.array(test_load_mat['L'])

        return x_train1, y_train1, x_test1, y_test1, N, N_test, H, L