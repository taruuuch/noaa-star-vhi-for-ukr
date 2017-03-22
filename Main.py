#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function


import pandas as pd
import urllib2
import glob, os

from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show, legend
from datetime import date

csv_v = pd.read_csv('vhi/vhi_id_11.csv', delimiter=' ')
csv_p = pd.read_csv('percent/percent_id_11.csv', delimiter=' ')

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
    os.chdir("vhi")
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
                                 'year week SMN SMT VCI TCI VHI\n')
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
                                 'year week 0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100\n')
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


def parser_file(province_id, year_start, year_end, t_type):
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&" \
          + "provinceID=" + str(province_id) \
          + "&year1=" + str(year_start) \
          + "&year2=" + str(year_end) \
          + "&type=" + str(t_type)
    vhi_url = urllib2.urlopen(url)

    if (t_type == 'Mean'):
        out = open('../vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = '../vhi/vhi_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_vhi(s_file)
        except ZeroDivisionError:
            print(ZeroDivisionError.message)
    elif (t_type == 'VHI_Parea'):
        out = open('../percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        try:
            s_file = '../percent/percent_id_' + str(province_id) + '_' + str(date.today()) + '.csv'
            fix_file_percent(s_file)
        except ZeroDivisionError:
            print(ZeroDivisionError.message)


def analyzing_by_year(year):
    list_week = csv_v["week"][(csv_v["year"]) == year]
    list_vhi = csv_v["VHI"][(csv_v["year"]) == year]

    figure()
    plot(list_week, list_vhi, 'r')
    xlabel('week')
    ylabel('vhi')
    title('Graphic VHI for ' + str(year) + ' years')
    show()

    print(66 * "-")
    print("1. Minimum VHI")
    print("2. Maximum VHI")
    print(66 * "-")

    choose = input("Enter choose: ")

    if choose == 1:
        print(min((csv_v['VHI'][(csv_v["year"]) == year])))
    elif choose == 2:
        print(max(csv_v['VHI'][(csv_v["year"]) == year]))


def analyzing_by_two_year(year_1, year_2):
    list_week1 = csv_v["week"][(csv_v["year"]) == year_1]
    list_vhi1 = csv_v["VHI"][(csv_v["year"]) == year_1]
    list_week2 = csv_v["week"][(csv_v["year"]) == year_2]
    list_vhi2 = csv_v["VHI"][(csv_v["year"]) == year_2]

    figure()
    plot(list_week1, list_vhi1, 'r', label=str(year_1))
    plot(list_week2, list_vhi2, 'g', label=str(year_2))
    legend(loc=2)
    xlabel('week')
    ylabel('vhi')
    title('Graphic VHI for ' + str(year_1) + ',' + str(year_2) + ' years')
    show()


def choose_default_files(province_id, date_in):
    csv_v = pd.read_csv('../vhi/vhi_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')
    csv_p = pd.read_csv('../percent/percent_id_' + str(province_id) + '_' + str(date_in) + '.csv', delimiter=' ')


def sorting_by_ext_md(year):
    i = 10
    while i <= 30:
        x = str(
            csv_p['0'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['5'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['10'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['15'][((csv_p["year"]) == year) & (csv_p["week"] == i)]
        )
        if (x <= 15):
            print("Week: " + str(i) + ";\nExtreme!\nVHI: " + x + ";")
        i += 1

    i = 10
    while i <= 30:
        x = x = str(
            csv_p['0'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['5'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['10'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['15'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['20'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['25'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['30'][((csv_p["year"]) == year) & (csv_p["week"] == i)] +
            csv_p['35'][((csv_p["year"]) == year) & (csv_p["week"] == i)]
        )
        if (x <= 35):
            print("Week: " + str(i) + ";\nModerate!\nVHI: " + x + ";")
        i += 1


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
    print("6. ")
    print("7. ")
    print("8. ")
    print("9. ")
    print("0. Exit")
    print(70 * "-")


def main():
    files_in_directory()
    province_id = input("Enter province id: ")
    date_in = raw_input("Input date (yyyy-mm-dd): ")
    choose_default_files(province_id, date_in)

    clear_console()

    loop = True

    while loop:
        print_menu()

        choose = input("Enter your choose: ")

        if choose == 1:
            print(list_province)
            province_id = input("Choose province and input him [id] (1st column): ")
            year_start = input("Input start year: ")
            year_end = input("Input end year: ")
            choose = input("Choose type: \n1 - Mean; \n2 - VHI_Parea; ")
            if (choose == 1):
                t_type = 'Mean'
                parser_file(province_id, year_start, year_end, t_type)
            elif (choose == 2):
                t_type = 'VHI_Parea'
                parser_file(province_id, year_start, year_end, t_type)
        elif choose == 2:
            files_in_directory()
            province_id = input("Enter province id: ")
            date_in = raw_input("Input date (yyyy-mm-dd): ")
            choose_default_files(province_id, date_in)
        elif choose == 3:
            year = input("Enter first year: ")
            analyzing_by_year(year)
        elif choose == 4:
            year_1 = input("Enter first year: ")
            year_2 = input("Enter second year: ")
            analyzing_by_two_year(year_1, year_2)
        elif choose == 5:
            year = input("Input year: ")
            sorting_by_ext_md(year)
        elif choose == 0:
            loop = False


if __name__ == '__main__':
    main()
