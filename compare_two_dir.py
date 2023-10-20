from compare import compare_two_files
import typing as tp
import numpy as np
import os


def ratio_dir(matrix):
    flag = 1
    identic = []
    quite_similar = []
    not_similar = []
    for index_1, ratio_file in enumerate(matrix):
        for index_2, ratio in enumerate(ratio_file):
            if ratio == 1:
                flag = 0
                identic.append([index_1, index_2, ratio])
            elif ratio != 0:
                flag = 0
                quite_similar.append([index_1, index_2, ratio])
        if flag == 1:
            not_similar.append([index_1])
    return identic, quite_similar, not_similar


def compare_directories(directory_1, directory_2):
    file_list_1: tp.List[str] = os.listdir(directory_1)
    file_list_2 = os.listdir(directory_2)
    matrix = np.ndarray((len(file_list_1), len(file_list_2)))
    for index_1, file_1 in enumerate(file_list_1):
        for index_2, file_2 in enumerate(file_list_2):
            full_path_1 = directory_1 + '/' + file_1
            full_path_2 = directory_2 + '/' + file_2
            ratio = compare_two_files(full_path_1, full_path_2)
            matrix[index_1][index_2] = ratio

    ratio_first = ratio_dir(matrix)
    ratio_second = ratio_dir(matrix.T)

    for sim_files in ratio_first[0]:
        print(directory_1 + '/' + file_list_1[sim_files[0]] + ' - ' + directory_2 + '/' +
              file_list_2[
                  sim_files[
                      1]])
    for quite_sim in ratio_first[1]:
        print(directory_1 + '/' + file_list_1[quite_sim[0]] + ' - ' + directory_2 + '/' +
              file_list_2[
                  quite_sim[1]],
              quite_sim[2])
    for not_sim in ratio_first[2]:
        print(directory_1 + '/' + file_list_1[not_sim[0]] + " is not in " + directory_2)
    for not_sim in ratio_second[2]:
        print(directory_2 + '/' + file_list_2[not_sim[0]] + " is not in " + directory_1)
