#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from numpy import genfromtxt

from urllib.request import urlopen
import glob, os

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show, legend
from datetime import date

list_province = [[1, 'Cherkasy'],
                 [2, 'Chernihiv'],
                 [3, 'Chernivtsi'],
                 [4, 'Crimea'],
                 [5, 'Dnipropetrovsk'],
                 [6, 'Donetsk'],
                 [7, 'Ivano-Frankivsk'],
                 [8, 'Kharkiv'],
                 [9, 'Kherson'],
                 [10, 'Khmelnytskyy'],
                 [11, 'Kiev'],
                 [12, 'Kiev City'],
                 [13, 'Kirovohrad'],
                 [14, 'Luhansk'],
                 [15, 'Lviv'],
                 [16, 'Mykolayiv'],
                 [17, 'Odessa'],
                 [18, 'Poltava'],
                 [19, 'Rivne'],
                 [20, 'Sevastopol'],
                 [21, 'Sumy'],
                 [22, 'Ternopil'],
                 [23, 'Transcarpathia'],
                 [24, 'Vinnytsya'],
                 [25, 'Volyn'],
                 [26, 'Zaporizhzhya'],
                 [27, 'Zhytomyr']]


def files_in_directory():
    try:
        os.chdir("vhi")
        print("- vhi")
        for file in glob.glob("*.csv"):
            print(file)
    except:
        os.chdir("../vhi")
        print("- vhi")
        for file in glob.glob("*.csv"):
            print(file)
    os.chdir("../percent")
    print("- percent")
    for file in glob.glob("*.csv"):
        print(file)


def fix_file_vhi(s_file):
    fi = open(s_file)
    line = fi.readlines()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[0],
                                 '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(',', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('  ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('  ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi = open(s_file)
    line = fi.readlines()
    x = len(line)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[x - 1], '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()


def fix_file_percent(s_file):
    fi = open(s_file)
    line = fi.readlines()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[0],
                                 '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(',', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('   ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace('  ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(' ', ' ')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi = open(s_file)
    line = fi.readlines()
    x = len(line)
    with open(s_file, 'r+') as f:
        f_str = f.read().replace(line[x - 1], '')
        f.seek(0)
        f.truncate()
        f.write(f_str)
    fi.close()


def parser_file(province_id):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&" \
          + "provinceID=" + str(province_id) \
          + "&year1=1981&year2=2017&type=Mean"
    vhi_url = urlopen(url)

    try:
        out = open('../vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = '../vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
        except:
            s_file = 'vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
    except:
        out = open('vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = 'vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
        except:
            s_file = '../vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)

    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&" \
          + "provinceID=" + str(province_id) \
          + "&year1=1981&year2=2017&type=VHI_Parea"
    vhi_url = urlopen(url)

    try:
        out = open('percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = 'percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_percent(s_file)
        except:
            s_file = '../percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_percent(s_file)
    except:
        out = open('../percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = '../percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_percent(s_file)
        except:
            s_file = 'percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_percent(s_file)


def analyzing_by_year(year, csv_v):
    list_week = []
    list_vhi = []

    c = 0

    for bich in csv_v:
        if (csv_v[c][0] == year):
            list_week.append(csv_v[c][1])
            list_vhi.append(csv_v[c][6])
        c += 1

    figure()
    plot(list_week, list_vhi, 'r')
    xlabel('week')
    ylabel('vhi')
    title('Graphic VHI for ' + str(year) + ' year')
    show()

    print(66 * "-")
    print("1. Minimum VHI")
    print("2. Maximum VHI")
    print(66 * "-")

    choose = input("Enter choose: ")

    if choose == 1:
        print(min(list_vhi))
    elif choose == 2:
        print(max(list_vhi))


def analyzing_by_two_year(year_1, year_2, csv_v):
    list_week1 = []
    list_vhi1 = []
    list_week2 = []
    list_vhi2 = []

    c = 0
    for bich in csv_v:
        if (csv_v[c][0] == year_1):
            list_week1.append(csv_v[c][1])
            list_vhi1.append(csv_v[c][6])
        elif (csv_v[c][0] == year_2):
            list_week2.append(csv_v[c][1])
            list_vhi2.append(csv_v[c][6])
        c += 1

    figure()
    plot(list_week1, list_vhi1, 'r', label=str(year_1))
    plot(list_week2, list_vhi2, 'g', label=str(year_2))
    legend(loc=2)
    xlabel('week')
    ylabel('vhi')
    title('Graphic VHI for ' + str(year_1) + ',' + str(year_2) + ' years')
    show()


def choose_default_vhi(province_id, date_in):
    try:
        csv_v = genfromtxt('vhi/vhi_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    except:
        csv_v = genfromtxt('../vhi/vhi_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    return csv_v


def choose_default_percent(province_id, date_in):
    try:
        csv_p = genfromtxt('percent/percent_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    except:
        csv_p = genfromtxt('../percent/percent_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    return csv_p


def sorting_by_ext_md(year, csv_p):
    print("*" * 10, "Moderate", "*" * 10)

    x = []
    w = []

    c = 0
    for bich in csv_p:
        if (csv_p[c][0] == year):
            x.append(csv_p[c][2] + csv_p[c][3] + csv_p[c][4] + csv_p[c][5])
            w.append(csv_p[c][1])
        c += 1

    c = 0
    for bich in x:
        if (x[c] <= 30):
            print("Week: " + str(w[c]) + "; Extreme!")
        c += 1

    print("*" * 10, "Moderate", "*" * 10)

    x = []
    w = []

    c = 0
    for bich in csv_p:
        if (csv_p[c][0] == year):
            x.append(csv_p[c][2] + csv_p[c][3] + csv_p[c][4] + csv_p[c][5] + csv_p[c][6] + csv_p[c][7] + csv_p[c][8]
                     + csv_p[c][9])
            w.append(csv_p[c][1])
        c += 1

    c = 0
    for bich in x:
        if (x[c] <= 50):
            if (x[c] > 30):
                print("Week: " + str(w[c]) + "; Moderate!")
        c += 1


def clear_console():
    try:
        os.system('clear')
    except:
        os.system('cls')


def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Parse data")
    print("2. Re-choose files")
    print("3. Graphic for one year")
    print("4. Graphic for two years")
    print("5. Sorting")
    print("0. Exit")
    print(70 * "-")


def main():
    csv_v = choose_default_vhi("4", "2017-03-29")
    csv_p = choose_default_percent("4", "2017-03-29")

    loop = True

    while loop:
        print_menu()

        choose = input("Enter your choose: ")

        if choose == 1:
            print(list_province)
            province_id = input("Choose province and input him [id] (1st column): ")
            parser_file(province_id)
            files_in_directory()
            province_id = input("Enter province id: ")
            date_in = raw_input("Input date (yyyy-mm-dd): ")
            csv_v = choose_default_vhi(province_id, date_in)
            csv_p = choose_default_percent(province_id, date_in)
        elif choose == 2:
            files_in_directory()
            province_id = input("Enter province id: ")
            date_in = raw_input("Input date (yyyy-mm-dd): ")
            csv_v = choose_default_vhi(province_id, date_in)
            csv_p = choose_default_percent(province_id, date_in)
        elif choose == 3:
            year = input("Enter year: ")
            analyzing_by_year(year, csv_v)
        elif choose == 4:
            year_1 = input("Enter first year: ")
            year_2 = input("Enter second year: ")
            analyzing_by_two_year(year_1, year_2, csv_v)
        elif choose == 5:
            year = input("Input year: ")
            sorting_by_ext_md(year, csv_p)
        elif choose == 0:
            loop = False


if __name__ == '__main__':
    main()
