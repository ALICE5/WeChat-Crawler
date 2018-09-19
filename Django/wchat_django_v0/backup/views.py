from django.shortcuts import render
import pandas as pd
import json
import numpy as np
import urllib.request
from datetime import datetime

datafile_path = "./analysis/data_csv/XinHuaShe_Merge_Final.csv"
datafile_path2 = "./analysis/data_csv/XinHuaShe_Final2.csv"


def slice_date(details, after_year, after_month, after_day, before_year, before_month, before_day):
    """
    没找到时间切片的方法
    :param details:
    :param after_year: x年之后
    :param after_month: x月之后
    :param after_day: x日之后(包含x日)
    :param before_year: x年之前
    :param before_month: x月之前
    :param before_day: x日之前(不包含x日)
    :return:
    """

    before_date = details[details["date"] < pd.datetime(before_year, before_month, before_day)]
    details_date = before_date[details["date"] >= pd.datetime(after_year, after_month, after_day)]
    return details_date


# Create your views here.
def Cover(request):
    context = {
    }
    return render(request, 'cover.html', context)


def App_view(request):
    context = {
    }
    return render(request, 'app_view.html', context)


def Page1_1(request):
    # 将csv中的date转换为datetime类型可供分析
    details = pd.read_csv(datafile_path2)
    details['date'] = pd.to_datetime(details['date'])

    # 7日数据
    day1 = slice_date(details, 2018, 8, 20, 2018, 8, 21)
    day2 = slice_date(details, 2018, 8, 21, 2018, 8, 22)
    day3 = slice_date(details, 2018, 8, 22, 2018, 8, 23)
    day4 = slice_date(details, 2018, 8, 23, 2018, 8, 24)
    day5 = slice_date(details, 2018, 8, 24, 2018, 8, 25)
    day6 = slice_date(details, 2018, 8, 25, 2018, 8, 26)
    day7 = slice_date(details, 2018, 8, 26, 2018, 8, 27)

    # day_count_list 为日发文数
    day_count_list = {
        "day1": day1["title"].count(),
        "day2": day2["title"].count(),
        "day3": day3["title"].count(),
        "day4": day4["title"].count(),
        "day5": day5["title"].count(),
        "day6": day6["title"].count(),
        "day7": day7["title"].count()
    }
    # 每日点赞数
    day_likeNum_list = {
        "day1": sum(day1["likeNum"]),
        "day2": sum(day2["likeNum"]),
        "day3": sum(day3["likeNum"]),
        "day4": sum(day4["likeNum"]),
        "day5": sum(day5["likeNum"]),
        "day6": sum(day6["likeNum"]),
        "day7": sum(day7["likeNum"])
    }
    # 每日评论数
    day_comment_list = {
        "day1": sum(day1["elected_comment_total_cnt"]),
        "day2": sum(day2["elected_comment_total_cnt"]),
        "day3": sum(day3["elected_comment_total_cnt"]),
        "day4": sum(day4["elected_comment_total_cnt"]),
        "day5": sum(day5["elected_comment_total_cnt"]),
        "day6": sum(day6["elected_comment_total_cnt"]),
        "day7": sum(day7["elected_comment_total_cnt"])
    }
    # 每日阅读数
    day_readNum_list = {
        "day1": sum(day1["readnum_random"]),
        "day2": sum(day2["readnum_random"]),
        "day3": sum(day3["readnum_random"]),
        "day4": sum(day4["readnum_random"]),
        "day5": sum(day5["readnum_random"]),
        "day6": sum(day6["readnum_random"]),
        "day7": sum(day7["readnum_random"])
    }
    date = {"day1": "2018.8.21",
            "day2": "2018.8.22",
            "day3": "2018.8.23",
            "day4": "2018.8.24",
            "day5": "2018.8.25",
            "day6": "2018.8.26",
            "day7": "2018.8.27"}
    one_week_list = []
    date_num = []
    view = []
    like = []
    comment = []
    count = []
    for item in ["day1", "day2", "day3", "day4", "day5", "day6", "day7"]:
        list = {
            "time": date[item],
            "view_num": str(day_readNum_list[item]),
            "like_num": str(day_likeNum_list[item]),
            "comment_num": str(day_comment_list[item]),
            "count": str(day_count_list[item]),
            "view_mean": str(int(day_readNum_list[item] / day_count_list[item])),
            "like_mean": str(int(day_likeNum_list[item] / day_count_list[item]))
        }
        date_num.append(date[item])
        view.append(int(day_readNum_list[item]))
        like.append(int(day_likeNum_list[item]))
        comment.append(int(day_comment_list[item]))
        count.append(int(day_count_list[item]))
        one_week_list.append(list)
    with open("./analysis/static/json/page1_1_table.json", "w", encoding='utf-8') as f:
        json.dump(one_week_list, f, ensure_ascii=False)

    last_day_list = one_week_list[6]
    the_day_before_yesterday = one_week_list[5]
    context = {
        "view_num": "{:0.2f}".format(int(last_day_list["view_num"]) / 100000000) + "亿",
        # "view_num": last_day_list["view_num"],
        "like_num": last_day_list["like_num"],
        "comment_num": last_day_list["comment_num"],
        "count_num": last_day_list["count"],
        "view_num1": '{:.2%}'.format((int(last_day_list["view_num"]) - int(the_day_before_yesterday["view_num"])) / int(
            the_day_before_yesterday["view_num"])),
        "like_num1": '{:.2%}'.format((int(last_day_list["like_num"]) - int(the_day_before_yesterday["like_num"])) / int(
            the_day_before_yesterday["like_num"])),
        "comment_num1": '{:.2%}'.format(
            (int(last_day_list["comment_num"]) - int(the_day_before_yesterday["comment_num"])) / int(
                the_day_before_yesterday["comment_num"])),
        "count1": '{:.2%}'.format((int(last_day_list["count"]) - int(the_day_before_yesterday["count"])) / int(
            the_day_before_yesterday["count"])),
        "date_num": date_num,
        "view": view,
        "like": like,
        "comment": comment,
        "count": count
    }
    return render(request, 'page1_1.html', context)


def Page1_2(request):
    # 将csv中的date转换为datetime类型可供分析
    details = pd.read_csv(datafile_path2)
    details['date'] = pd.to_datetime(details['date'])
    week1 = slice_date(details, 2018, 3, 12, 2018, 3, 19)
    week2 = slice_date(details, 2018, 3, 19, 2018, 3, 26)
    week3 = slice_date(details, 2018, 3, 26, 2018, 4, 2)
    week4 = slice_date(details, 2018, 4, 2, 2018, 4, 9)
    week5 = slice_date(details, 2018, 4, 9, 2018, 4, 16)
    week6 = slice_date(details, 2018, 4, 16, 2018, 4, 23)
    week7 = slice_date(details, 2018, 4, 23, 2018, 4, 30)
    week8 = slice_date(details, 2018, 4, 30, 2018, 5, 7)
    week9 = slice_date(details, 2018, 5, 7, 2018, 5, 14)
    week10 = slice_date(details, 2018, 5, 14, 2018, 5, 21)
    week11 = slice_date(details, 2018, 5, 21, 2018, 5, 28)
    week12 = slice_date(details, 2018, 5, 28, 2018, 6, 4)
    week13 = slice_date(details, 2018, 6, 4, 2018, 6, 11)
    week14 = slice_date(details, 2018, 6, 11, 2018, 6, 18)
    week15 = slice_date(details, 2018, 6, 18, 2018, 6, 25)
    week16 = slice_date(details, 2018, 6, 25, 2018, 7, 2)
    weekend1 = slice_date(details, 2018, 7, 2, 2018, 7, 9)
    weekend2 = slice_date(details, 2018, 7, 9, 2018, 7, 16)
    weekend3 = slice_date(details, 2018, 7, 16, 2018, 7, 23)
    weekend4 = slice_date(details, 2018, 7, 23, 2018, 7, 30)
    weekend5 = slice_date(details, 2018, 7, 30, 2018, 8, 6)
    weekend6 = slice_date(details, 2018, 8, 6, 2018, 8, 13)
    weekend7 = slice_date(details, 2018, 8, 13, 2018, 8, 20)
    weekend8 = slice_date(details, 2018, 8, 20, 2018, 8, 27)
    # wenkend_count_list 为周发文数
    weekend_count_list = {
        "0312-0319": week1["title"].count(),
        "0319-0326": week2["title"].count(),
        "0326-0402": week3["title"].count(),
        "0402-0409": week4["title"].count(),
        "0409-0416": week5["title"].count(),
        "0416-0423": week6["title"].count(),
        "0423-0430": week7["title"].count(),
        "0430-0507": week8["title"].count(),
        "0507-0514": week9["title"].count(),
        "0514-0521": week10["title"].count(),
        "0521-0528": week11["title"].count(),
        "0528-0604": week12["title"].count(),
        "0604-0611": week13["title"].count(),
        "0611-0618": week14["title"].count(),
        "0618-0625": week15["title"].count(),
        "0625-0702": week16["title"].count(),
        "0702-0709": weekend1["title"].count(),
        "0709-0716": weekend2["title"].count(),
        "0716-0723": weekend3["title"].count(),
        "0723-0730": weekend4["title"].count(),
        "0731-0806": weekend5["title"].count(),
        "0806-0813": weekend6["title"].count(),
        "0813-0820": weekend7["title"].count(),
        "0820-0827": weekend8["title"].count()
    }
    # 周点赞数
    weekend_likeNum_list = {
        "0312-0319": sum(week1["likeNum"]),
        "0319-0326": sum(week2["likeNum"]),
        "0326-0402": sum(week3["likeNum"]),
        "0402-0409": sum(week4["likeNum"]),
        "0409-0416": sum(week5["likeNum"]),
        "0416-0423": sum(week6["likeNum"]),
        "0423-0430": sum(week7["likeNum"]),
        "0430-0507": sum(week8["likeNum"]),
        "0507-0514": sum(week9["likeNum"]),
        "0514-0521": sum(week10["likeNum"]),
        "0521-0528": sum(week11["likeNum"]),
        "0528-0604": sum(week12["likeNum"]),
        "0604-0611": sum(week13["likeNum"]),
        "0611-0618": sum(week14["likeNum"]),
        "0618-0625": sum(week15["likeNum"]),
        "0625-0702": sum(week16["likeNum"]),
        "0702-0709": sum(weekend1["likeNum"]),
        "0709-0716": sum(weekend2["likeNum"]),
        "0716-0723": sum(weekend3["likeNum"]),
        "0723-0730": sum(weekend4["likeNum"]),
        "0731-0806": sum(weekend5["likeNum"]),
        "0806-0813": sum(weekend6["likeNum"]),
        "0813-0820": sum(weekend7["likeNum"]),
        "0820-0827": sum(weekend8["likeNum"])
    }
    # 周评论数
    weekend_comment_list = {
        "0312-0319": sum(week1["elected_comment_total_cnt"]),
        "0319-0326": sum(week2["elected_comment_total_cnt"]),
        "0326-0402": sum(week3["elected_comment_total_cnt"]),
        "0402-0409": sum(week4["elected_comment_total_cnt"]),
        "0409-0416": sum(week5["elected_comment_total_cnt"]),
        "0416-0423": sum(week6["elected_comment_total_cnt"]),
        "0423-0430": sum(week7["elected_comment_total_cnt"]),
        "0430-0507": sum(week8["elected_comment_total_cnt"]),
        "0507-0514": sum(week9["elected_comment_total_cnt"]),
        "0514-0521": sum(week10["elected_comment_total_cnt"]),
        "0521-0528": sum(week11["elected_comment_total_cnt"]),
        "0528-0604": sum(week12["elected_comment_total_cnt"]),
        "0604-0611": sum(week13["elected_comment_total_cnt"]),
        "0611-0618": sum(week14["elected_comment_total_cnt"]),
        "0618-0625": sum(week15["elected_comment_total_cnt"]),
        "0625-0702": sum(week16["elected_comment_total_cnt"]),
        "0702-0709": sum(weekend1["elected_comment_total_cnt"]),
        "0709-0716": sum(weekend2["elected_comment_total_cnt"]),
        "0716-0723": sum(weekend3["elected_comment_total_cnt"]),
        "0723-0730": sum(weekend4["elected_comment_total_cnt"]),
        "0731-0806": sum(weekend5["elected_comment_total_cnt"]),
        "0806-0813": sum(weekend6["elected_comment_total_cnt"]),
        "0813-0820": sum(weekend7["elected_comment_total_cnt"]),
        "0820-0827": sum(weekend8["elected_comment_total_cnt"])
    }
    # 周阅读数
    weekend_readNum_list = {
        "0312-0319": sum(week1["readnum_random"]),
        "0319-0326": sum(week2["readnum_random"]),
        "0326-0402": sum(week3["readnum_random"]),
        "0402-0409": sum(week4["readnum_random"]),
        "0409-0416": sum(week5["readnum_random"]),
        "0416-0423": sum(week6["readnum_random"]),
        "0423-0430": sum(week7["readnum_random"]),
        "0430-0507": sum(week8["readnum_random"]),
        "0507-0514": sum(week9["readnum_random"]),
        "0514-0521": sum(week10["readnum_random"]),
        "0521-0528": sum(week11["readnum_random"]),
        "0528-0604": sum(week12["readnum_random"]),
        "0604-0611": sum(week13["readnum_random"]),
        "0611-0618": sum(week14["readnum_random"]),
        "0618-0625": sum(week15["readnum_random"]),
        "0625-0702": sum(week16["readnum_random"]),
        "0702-0709": sum(weekend1["readnum_random"]),
        "0709-0716": sum(weekend2["readnum_random"]),
        "0716-0723": sum(weekend3["readnum_random"]),
        "0723-0730": sum(weekend4["readnum_random"]),
        "0731-0806": sum(weekend5["readnum_random"]),
        "0806-0813": sum(weekend6["readnum_random"]),
        "0813-0820": sum(weekend7["readnum_random"]),
        "0820-0827": sum(weekend8["readnum_random"])
    }
    one_week_list = []
    date = ["0312-0319", "0319-0326", "0326-0402", "0402-0409", "0409-0416", "0416-0423", "0423-0430", "0430-0507",
            "0507-0514", "0514-0521", "0521-0528", "0528-0604", "0604-0611", "0611-0618", "0618-0625", "0625-0702",
            "0702-0709", "0709-0716", "0716-0723", "0723-0730", "0731-0806", "0806-0813", "0813-0820", "0820-0827"]

    for item in date:
        list = {
            "time": item,
            "view_num": str(weekend_readNum_list[item]),
            "like_num": str(weekend_likeNum_list[item]),
            "comment_num": str(weekend_comment_list[item]),
            "count": str(weekend_count_list[item]),
            "view_mean": str(int(weekend_readNum_list[item] / weekend_count_list[item])),
            "like_mean": str(int(weekend_likeNum_list[item] / weekend_count_list[item]))
        }
        one_week_list.append(list)

    with open("./analysis/static/json/page1_2_table.json", "w", encoding='utf-8') as f:
        json.dump(one_week_list, f, ensure_ascii=False)
    context = {
        'weekend_count_list': weekend_count_list,
        "weekend_likeNum_list": weekend_likeNum_list,
        "weekend_comment_list": weekend_comment_list,
        "weekend_readNum_list": weekend_readNum_list,
        "date": date
    }
    return render(request, 'page1_2.html', context)


def Page2_1(request):
    context = {
    }
    return render(request, 'page2_1.html', context)


def Page2_2(request):
    # 读取csv中的数据
    details = pd.read_csv(datafile_path)
    details['date'] = pd.to_datetime(details['date'])
    before_date = details[details["date"] < pd.datetime(2018, 9, 1)]
    details = before_date[details["date"] >= pd.datetime(2018, 8, 1)]
    details_clean = details[details['author'] != "0"]
    details = details_clean.dropna()
    # print(details_clean['author'])
    # 数据分析
    anthor_list = []
    for i in details['author']:
        anthor_list.append(i)
    anthor_sort = pd.value_counts(anthor_list)
    author_month_list = []
    author_month_chart = []
    for key, value in anthor_sort.items():
        papers = details[details['author'] == key]
        data = {
            "author": key,
            "papernums": value,
            "likeNum": sum(papers['likeNum']),
            "mean_likeNum": int(np.mean(papers['likeNum'])),
            "readNum": sum(papers['readNum_handle']),
            "mean_readNum": int(np.mean(papers['readNum_handle'])),
            "commentNum": sum(papers['elected_comment_total_cnt'])
        }
        data_chart = {
            "author": key,
            "likeNum": sum(papers['likeNum']),
            "commentNum": sum(papers['elected_comment_total_cnt'])
        }
        author_month_list.append(data)
        author_month_chart.append(data_chart)
    with open("./analysis/static/json/page2-2-table.json", "w", encoding='utf-8') as f:
        json.dump(author_month_list, f, ensure_ascii=False)
    context = {
        "author_month_list": author_month_list,
        "author_month_chart": author_month_chart
    }
    return render(request, 'page2_2.html', context)


def Page2_3(request):
    # 读取csv中的数据
    details = pd.read_csv(datafile_path)
    details['date'] = pd.to_datetime(details['date'])
    before_date = details[details["date"] < pd.datetime(2018, 9, 1)]
    details = before_date[details["date"] >= pd.datetime(2018, 3, 1)]
    details_clean = details[details['author'] != "0"]
    details = details_clean.dropna()
    # print(details_clean['author'])
    # 数据分析
    anthor_list = []
    for i in details['author']:
        anthor_list.append(i)
    anthor_sort = pd.value_counts(anthor_list)
    author_month_list = []
    author_month_chart = []
    for key, value in anthor_sort.items():
        papers = details[details['author'] == key]
        data = {
            "author": key,
            "papernums": value,
            "likeNum": sum(papers['likeNum']),
            "mean_likeNum": int(np.mean(papers['likeNum'])),
            "readNum": sum(papers['readNum_handle']),
            "mean_readNum": int(np.mean(papers['readNum_handle'])),
            "commentNum": sum(papers['elected_comment_total_cnt'])
        }
        data_chart = {
            "author": key,
            "likeNum": sum(papers['likeNum']),
            "commentNum": sum(papers['elected_comment_total_cnt'])
        }
        author_month_list.append(data)
        author_month_chart.append(data_chart)
    context = {
        "author_month_list": author_month_list,
        "author_month_chart": author_month_chart
    }
    with open("./analysis/static/json/page2-3-table.json", "w", encoding='utf-8') as f:
        json.dump(author_month_list, f, ensure_ascii=False)
    return render(request, 'page2_3.html', context)


def Page3_1(request):
    # 将csv中的date转换为datetime类型可供分析
    details = pd.read_csv(datafile_path2, keep_default_na=False)
    details['date'] = pd.to_datetime(details['date'])
    count_type_sum = details.iloc[:, 0].size
    count_type_original = int(sum(details["author"] == "0")) + int(sum(details["author"] == ""))
    count_type_reprint = count_type_sum - count_type_original

    # 原创
    original_details = details[(details["author"] == "0") | (details["author"] == "")]

    original_details_one = slice_date(original_details, 2018, 8, 30, 2018, 8, 31)
    original_details_two = slice_date(original_details, 2018, 8, 31, 2018, 9, 1)
    original_details_three = slice_date(original_details, 2018, 9, 1, 2018, 9, 2)
    original_details_four = slice_date(original_details, 2018, 9, 2, 2018, 9, 3)
    original_details_five = slice_date(original_details, 2018, 9, 3, 2018, 9, 4)
    original_details_six = slice_date(original_details, 2018, 9, 4, 2018, 9, 5)
    original_details_seven = slice_date(original_details, 2018, 9, 5, 2018, 9, 6)
    original_details_sevendays = slice_date(original_details, 2018, 8, 30, 2018, 9, 6)
    # 原创 浏览数、平均浏览数
    count_original_readNum_list = {
        "count_original_one_readNum": sum(original_details_one["readnum_random"]),
        "count_original_two_readNum": sum(original_details_two["readnum_random"]),
        "count_original_three_readNum": sum(original_details_three["readnum_random"]),
        "count_original_four_readNum": sum(original_details_four["readnum_random"]),
        "count_original_five_readNum": sum(original_details_five["readnum_random"]),
        "count_original_six_readNum": sum(original_details_six["readnum_random"]),
        "count_original_seven_readNum": sum(original_details_seven["readnum_random"]),
        "count_original_readNum_mean": sum(original_details_sevendays["readnum_random"] / 7)
    }
    # original_sevendays_parpers = original_details_sevendays["guid"].count()

    # 非原创
    reprint_details = details[(details["author"] != "0") & (details["author"] != "")]
    # 非原创 浏览数、平均浏览数
    # count_reprint_details=count_sum()
    reprint_details_one = slice_date(reprint_details, 2018, 8, 30, 2018, 8, 31)
    reprint_details_two = slice_date(reprint_details, 2018, 8, 31, 2018, 9, 1)
    reprint_details_three = slice_date(reprint_details, 2018, 9, 1, 2018, 9, 2)
    reprint_details_four = slice_date(reprint_details, 2018, 9, 2, 2018, 9, 3)
    reprint_details_five = slice_date(reprint_details, 2018, 9, 3, 2018, 9, 4)
    reprint_details_six = slice_date(reprint_details, 2018, 9, 4, 2018, 9, 5)
    reprint_details_seven = slice_date(reprint_details, 2018, 9, 5, 2018, 9, 6)
    reprint_details_sevendays = slice_date(reprint_details, 2018, 8, 30, 2018, 9, 6)

    # 非原创阅读数
    count_reprint_readNum_list = {
        "count_reprint_one_readNum": sum(reprint_details_one["readnum_random"]),
        "count_reprint_two_readNum": sum(reprint_details_two["readnum_random"]),
        "count_reprint_three_readNum": sum(reprint_details_three["readnum_random"]),
        "count_reprint_four_readNum": sum(reprint_details_four["readnum_random"]),
        "count_reprint_five_readNum": sum(reprint_details_five["readnum_random"]),
        "count_reprint_six_readNum": sum(reprint_details_six["readnum_random"]),
        "count_reprint_seven_readNum": sum(reprint_details_seven["readnum_random"]),
        "count_reprint_readNum_mean": np.mean(reprint_details_sevendays["readnum_random"])
    }

    # 原创点赞数 平均点赞数
    count_original_likeNum_list = {
        "count_original_one_likeNum": sum(original_details_one["likeNum"]),
        "count_original_two_likeNum": sum(original_details_two["likeNum"]),
        "count_original_three_likeNum": sum(original_details_three["likeNum"]),
        "count_original_four_likeNum": sum(original_details_four["likeNum"]),
        "count_original_five_likeNum": sum(original_details_five["likeNum"]),
        "count_original_six_likeNum": sum(original_details_six["likeNum"]),
        "count_original_seven_likeNum": sum(original_details_seven["likeNum"]),
        "count_original_readNum_mean": np.mean(original_details_sevendays["likeNum"])
    }

    # 转载点赞数 平均点赞数
    count_reprint_likeNum_list = {
        "count_reprint_one_likeNum": sum(reprint_details_one["likeNum"]),
        "count_reprint_two_likeNum": sum(reprint_details_two["likeNum"]),
        "count_reprint_three_likeNum": sum(reprint_details_three["likeNum"]),
        "count_reprint_four_likeNum": sum(reprint_details_four["likeNum"]),
        "count_reprint_five_likeNum": sum(reprint_details_five["likeNum"]),
        "count_reprint_six_likeNum": sum(reprint_details_six["likeNum"]),
        "count_reprint_seven_likeNum": sum(reprint_details_seven["likeNum"]),
        "count_reprint_readNum_mean": np.mean(reprint_details_sevendays["likeNum"])
    }
    # 原创评论数
    count_original_comment_list = {
        "count_original_one_comment": sum(original_details_one["elected_comment_total_cnt"]),
        "count_original_two_comment": sum(original_details_two["elected_comment_total_cnt"]),
        "count_original_three_comment": sum(original_details_three["elected_comment_total_cnt"]),
        "count_original_four_comment": sum(original_details_four["elected_comment_total_cnt"]),
        "count_original_five_comment": sum(original_details_five["elected_comment_total_cnt"]),
        "count_original_six_comment": sum(original_details_six["elected_comment_total_cnt"]),
        "count_original_seven_comment": sum(original_details_seven["elected_comment_total_cnt"])
    }
    # 转载评论数
    count_reprint_comment_list = {
        "count_reprint_one_comment": sum(reprint_details_one["elected_comment_total_cnt"]),
        "count_reprint_two_comment": sum(reprint_details_two["elected_comment_total_cnt"]),
        "count_reprint_three_comment": sum(reprint_details_three["elected_comment_total_cnt"]),
        "count_reprint_four_comment": sum(reprint_details_four["elected_comment_total_cnt"]),
        "count_reprint_five_comment": sum(reprint_details_five["elected_comment_total_cnt"]),
        "count_reprint_six_comment": sum(reprint_details_six["elected_comment_total_cnt"]),
        "count_reprint_seven_comment": sum(reprint_details_seven["elected_comment_total_cnt"])
    }
    # 原创文章数
    count_original_paper_list = {
        "count_original_one_paper": str(original_details_one["elected_comment_total_cnt"].count()),
        "count_original_two_paper": str(original_details_two["elected_comment_total_cnt"].count()),
        "count_original_three_paper": str(original_details_three["elected_comment_total_cnt"].count()),
        "count_original_four_paper": str(original_details_four["elected_comment_total_cnt"].count()),
        "count_original_five_paper": str(original_details_five["elected_comment_total_cnt"].count()),
        "count_original_six_paper": str(original_details_six["elected_comment_total_cnt"].count()),
        "count_original_seven_paper": str(original_details_seven["elected_comment_total_cnt"].count())
    }
    # 转载文章数
    count_reprint_paper_list = {
        "count_reprint_one_paper": str(reprint_details_one["elected_comment_total_cnt"].count()),
        "count_reprint_two_paper": str(reprint_details_two["elected_comment_total_cnt"].count()),
        "count_reprint_three_paper": str(reprint_details_three["elected_comment_total_cnt"].count()),
        "count_reprint_four_paper": str(reprint_details_four["elected_comment_total_cnt"].count()),
        "count_reprint_five_paper": str(reprint_details_five["elected_comment_total_cnt"].count()),
        "count_reprint_six_paper": str(reprint_details_six["elected_comment_total_cnt"].count()),
        "count_reprint_seven_paper": str(reprint_details_seven["elected_comment_total_cnt"].count())
    }
    # 原创列表展示
    original_list = []
    original_day_one = {
        "date": "2018-8-30",
        "readNum": count_original_readNum_list["count_original_one_readNum"],
        "likeNum": count_original_likeNum_list["count_original_one_likeNum"],
        "comment": count_original_comment_list["count_original_one_comment"],
        "papers": count_original_paper_list["count_original_one_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_two = {
        "date": "2018-8-31",
        "readNum": count_original_readNum_list["count_original_two_readNum"],
        "likeNum": count_original_likeNum_list["count_original_two_likeNum"],
        "comment": count_original_comment_list["count_original_two_comment"],
        "papers": count_original_paper_list["count_original_two_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_three = {
        "date": "2018-9-1",
        "readNum": count_original_readNum_list["count_original_three_readNum"],
        "likeNum": count_original_likeNum_list["count_original_three_likeNum"],
        "comment": count_original_comment_list["count_original_three_comment"],
        "papers": count_original_paper_list["count_original_three_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_four = {
        "date": "2018-9-2",
        "readNum": count_original_readNum_list["count_original_four_readNum"],
        "likeNum": count_original_likeNum_list["count_original_four_likeNum"],
        "comment": count_original_comment_list["count_original_four_comment"],
        "papers": count_original_paper_list["count_original_four_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_five = {
        "date": "2018-9-3",
        "readNum": count_original_readNum_list["count_original_five_readNum"],
        "likeNum": count_original_likeNum_list["count_original_five_likeNum"],
        "comment": count_original_comment_list["count_original_five_comment"],
        "papers": count_original_paper_list["count_original_five_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_six = {
        "date": "2018-9-4",
        "readNum": count_original_readNum_list["count_original_six_readNum"],
        "likeNum": count_original_likeNum_list["count_original_six_likeNum"],
        "comment": count_original_comment_list["count_original_six_comment"],
        "papers": count_original_paper_list["count_original_six_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_day_seven = {
        "date": "2018-9-5",
        "readNum": count_original_readNum_list["count_original_seven_readNum"],
        "likeNum": count_original_likeNum_list["count_original_seven_likeNum"],
        "comment": count_original_comment_list["count_original_seven_comment"],
        "papers": count_original_paper_list["count_original_seven_paper"],
        "mean_readNum": int(count_original_readNum_list["count_original_readNum_mean"]),
        "mean_likeNum": int(count_original_likeNum_list["count_original_readNum_mean"])
    }
    original_list.append(original_day_one)
    original_list.append(original_day_two)
    original_list.append(original_day_three)
    original_list.append(original_day_four)
    original_list.append(original_day_five)
    original_list.append(original_day_six)
    original_list.append(original_day_seven)

    # fei原创列表展示
    reprint_list = []
    reprint_day_one = {
        "date": "2018-8-30",
        "readNum": str(count_reprint_readNum_list["count_reprint_one_readNum"]),
        "likeNum": str(count_reprint_likeNum_list["count_reprint_one_likeNum"]),
        "comment": str(count_reprint_comment_list["count_reprint_one_comment"]),
        "papers": str(count_reprint_paper_list["count_reprint_one_paper"]),
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_two = {
        "date": "2018-8-31",
        "readNum": count_reprint_readNum_list["count_reprint_two_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_two_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_two_comment"],
        "papers": count_reprint_paper_list["count_reprint_two_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_three = {
        "date": "2018-9-1",
        "readNum": count_reprint_readNum_list["count_reprint_three_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_three_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_three_comment"],
        "papers": count_reprint_paper_list["count_reprint_three_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_four = {
        "date": "2018-9-2",
        "readNum": count_reprint_readNum_list["count_reprint_four_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_four_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_four_comment"],
        "papers": count_reprint_paper_list["count_reprint_four_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_five = {
        "date": "2018-9-3",
        "readNum": count_reprint_readNum_list["count_reprint_five_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_five_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_five_comment"],
        "papers": count_reprint_paper_list["count_reprint_five_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_six = {
        "date": "2018-9-4",
        "readNum": count_reprint_readNum_list["count_reprint_six_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_six_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_six_comment"],
        "papers": count_reprint_paper_list["count_reprint_six_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_day_seven = {
        "date": "2018-9-5",
        "readNum": count_reprint_readNum_list["count_reprint_seven_readNum"],
        "likeNum": count_reprint_likeNum_list["count_reprint_seven_likeNum"],
        "comment": count_reprint_comment_list["count_reprint_seven_comment"],
        "papers": count_reprint_paper_list["count_reprint_seven_paper"],
        "mean_readNum": int(count_reprint_readNum_list["count_reprint_readNum_mean"]),
        "mean_likeNum": int(count_reprint_likeNum_list["count_reprint_readNum_mean"])
    }
    reprint_list.append(reprint_day_one)
    reprint_list.append(reprint_day_two)
    reprint_list.append(reprint_day_three)
    reprint_list.append(reprint_day_four)
    reprint_list.append(reprint_day_five)
    reprint_list.append(reprint_day_six)
    reprint_list.append(reprint_day_seven)
    date = ["2018-8-30", "2018-8-31", "2018-9-1", "2018-9-2", "2018-9-3", "2018-9-4", "2018-9-5"]
    with open("./analysis/static/json/page3-1-original.json", "w", encoding='utf-8') as f:
        json.dump(original_list, f, ensure_ascii=False)
    with open("./analysis/static/json/page3-1-reprint.json", "w", encoding='utf-8') as f:
        json.dump(reprint_list, f, ensure_ascii=False)
    context = {
        "count_type_original": count_type_original,
        "count_type_reprint": count_type_reprint,
        "count_original_readNum_list": [sum(original_details_one["readNum_handle"]),
                                        sum(original_details_two["readNum_handle"]),
                                        sum(original_details_three["readNum_handle"]),
                                        sum(original_details_four["readNum_handle"]),
                                        sum(original_details_five["readNum_handle"]),
                                        sum(original_details_six["readNum_handle"]),
                                        sum(original_details_seven["readNum_handle"])],

        "count_reprint_readNum_list": [sum(reprint_details_one["readNum_handle"]),
                                        sum(reprint_details_two["readNum_handle"]),
                                        sum(reprint_details_three["readNum_handle"]),
                                        sum(reprint_details_four["readNum_handle"]),
                                        sum(reprint_details_five["readNum_handle"]),
                                        sum(reprint_details_six["readNum_handle"]),
                                        sum(reprint_details_seven["readNum_handle"])],

        "count_original_likeNum_list": [sum(original_details_one["likeNum"]),
                                        sum(original_details_two["likeNum"]),
                                        sum(original_details_three["likeNum"]),
                                        sum(original_details_four["likeNum"]),
                                        sum(original_details_five["likeNum"]),
                                        sum(original_details_six["likeNum"]),
                                        sum(original_details_seven["likeNum"])],

        "count_reprint_likeNum_list": [sum(reprint_details_one["likeNum"]),
                                        sum(reprint_details_two["likeNum"]),
                                        sum(reprint_details_three["likeNum"]),
                                        sum(reprint_details_four["likeNum"]),
                                        sum(reprint_details_five["likeNum"]),
                                        sum(reprint_details_six["likeNum"]),
                                        sum(reprint_details_seven["likeNum"])],

        "count_original_comment_list": [sum(original_details_one["elected_comment_total_cnt"]),
                                        sum(original_details_two["elected_comment_total_cnt"]),
                                        sum(original_details_three["elected_comment_total_cnt"]),
                                        sum(original_details_four["elected_comment_total_cnt"]),
                                        sum(original_details_five["elected_comment_total_cnt"]),
                                        sum(original_details_six["elected_comment_total_cnt"]),
                                        sum(original_details_seven["elected_comment_total_cnt"])],

        "count_reprint_comment_list": [sum(reprint_details_one["elected_comment_total_cnt"]),
                                        sum(reprint_details_two["elected_comment_total_cnt"]),
                                        sum(reprint_details_three["elected_comment_total_cnt"]),
                                        sum(reprint_details_four["elected_comment_total_cnt"]),
                                        sum(reprint_details_five["elected_comment_total_cnt"]),
                                        sum(reprint_details_six["elected_comment_total_cnt"]),
                                        sum(reprint_details_seven["elected_comment_total_cnt"])],
        "count_original_paper_list": [int(original_details_one["elected_comment_total_cnt"].count()),
                                        int(original_details_two["elected_comment_total_cnt"].count()),
                                        int(original_details_three["elected_comment_total_cnt"].count()),
                                        int(original_details_four["elected_comment_total_cnt"].count()),
                                        int(original_details_five["elected_comment_total_cnt"].count()),
                                        int(original_details_six["elected_comment_total_cnt"].count()),
                                        int(original_details_seven["elected_comment_total_cnt"].count())],

        "count_reprint_paper_list": [int(reprint_details_one["elected_comment_total_cnt"].count()),
                                        int(reprint_details_two["elected_comment_total_cnt"].count()),
                                        int(reprint_details_three["elected_comment_total_cnt"].count()),
                                        int(reprint_details_four["elected_comment_total_cnt"].count()),
                                        int(reprint_details_five["elected_comment_total_cnt"].count()),
                                        int(reprint_details_six["elected_comment_total_cnt"].count()),
                                        int(reprint_details_seven["elected_comment_total_cnt"].count())],
        "date": date
    }
    return render(request, 'page3_1.html', context)


def Page3_2(request):
    details = pd.read_csv(datafile_path2)
    # 按点赞数倒序排名
    top_likeNum = details.sort_values(by="likeNum", ascending=False)
    top_ten_likeNum = top_likeNum.head(10)
    # 重新生成索引
    top_ten_likeNum = top_ten_likeNum.reset_index(drop=True)

    data_likeNum = []
    for index, row in top_ten_likeNum.iterrows():
        data_detail = {
            "id": str(index + 1),
            "title": row["title"],
            "likeNum": row["likeNum"],
            "date": row["date"],
        }
        data_likeNum.append(data_detail)

    # 按浏览数倒序排名
    top_readNum_handle = details.sort_values(by="readnum_random", ascending=False)
    top_ten_readNum_handle = top_readNum_handle.head(10)
    top_ten_readNum_handle = top_ten_readNum_handle.reset_index(drop=True)
    data_readNum_handle = []
    for index, row in top_ten_readNum_handle.iterrows():
        data_detail = {
            "id": str(index + 1),
            "title": row["title"],
            "readNum": row["readnum_random"],
            "date": row["date"],
        }
        data_readNum_handle.append(data_detail)

    # 按评论数倒序排名
    top_comment = details.sort_values(by="elected_comment_total_cnt", ascending=False)
    top_ten_comment = top_comment.head(10)
    top_ten_comment = top_ten_comment.reset_index(drop=True)
    data_comment = []
    for index, row in top_ten_comment.iterrows():
        data_detail = {
            "id": str(index + 1),
            "title": row["title"],
            "commentNum": row["elected_comment_total_cnt"],
            "date": row["date"],
        }
        data_comment.append(data_detail)

    # context = {
    #     "top_likeNum": data_likeNum,
    #     "top_readNum": data_readNum_handle,
    #     "top_comment": data_comment
    # }
    with open("./analysis/static/json/page3-2-likenum.json", "w", encoding='utf-8') as f:
        json.dump(data_likeNum, f, ensure_ascii=False)
    with open("./analysis/static/json/page3-2-readNum.json", "w", encoding='utf-8') as f:
        json.dump(data_readNum_handle, f, ensure_ascii=False)
    with open("./analysis/static/json/page3-2-comment.json", "w", encoding='utf-8') as f:
        json.dump(data_comment, f, ensure_ascii=False)
    return render(request, 'page3_2.html')


def Page4_1(request):
    context = {
    }
    return render(request, 'page4_1.html', context)


def Page4_2(request):
    context = {
    }
    return render(request, 'page4_2.html', context)

def Page4_3(request):
    commment_list = []
    sentiment_list = []

    file = open('./analysis/data_txt/result2.txt', 'r', encoding="utf-8")

    for i in file.readlines():
        if len(i.split('\t')) == 3:
            commment_list.append(i.split('\t')[0])
            sentiment_list.append(i.split('\t')[2].replace('\n', ""))

    df = pd.DataFrame({
        'commment': commment_list,
        'sentiment': sentiment_list,
    })

    df["sentiment"] = df["sentiment"].astype(float)
    index1 = df[(df["sentiment"] >= 0) & (df["sentiment"] < 0.1)]['commment'].count()
    index2 = df[(df["sentiment"] >= 0.1) & (df["sentiment"] < 0.2)]['commment'].count()
    index3 = df[(df["sentiment"] >= 0.2) & (df["sentiment"] < 0.3)]['commment'].count()
    index4 = df[(df["sentiment"] >= 0.3) & (df["sentiment"] < 0.4)]['commment'].count()
    index5 = df[(df["sentiment"] >= 0.4) & (df["sentiment"] < 0.5)]['commment'].count()
    index6 = df[(df["sentiment"] >= 0.5) & (df["sentiment"] < 0.6)]['commment'].count()
    index7 = df[(df["sentiment"] >= 0.6) & (df["sentiment"] < 0.7)]['commment'].count()
    index8 = df[(df["sentiment"] >= 0.7) & (df["sentiment"] < 0.8)]['commment'].count()
    index9 = df[(df["sentiment"] >= 0.8) & (df["sentiment"] < 0.9)]['commment'].count()
    index0 = df[(df["sentiment"] >= 0.9) & (df["sentiment"] <= 1)]['commment'].count()

    x = ['[0,0.1)', '[0.1,0.2)', '[0.2,0.3)', '[0.3,0.4)', '[0.4,0.5)', '[0.5,0.6)', '[0.6,0.7)', '[0.7,0.8)',
         '[0.8,0.9)', '[0.9,1.0]']
    y = [index1, index2, index3, index4, index5, index6, index7, index8, index9, index0]

    count_y = 0
    for  yy in y:
        count_y += yy

    pie = {"x": x, "y": y}

    df_sent = pd.read_table('./analysis/data_txt/result2.txt', names=['comment_content', 'create_time', 'sentiment'],
                            error_bad_lines=False,
                            sep='\t')
    df_sent.dropna(axis=0, how='any', inplace=True)
    df_sent = df_sent.reset_index()
    df_sent = df_sent.set_index('create_time')
    del df_sent['index']

    df_sent.index = [datetime.strptime(datetime.strptime(t, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'), '%Y-%m-%d') for t
                     in
                     df_sent.index]
    df_sent = df_sent.sort_index(ascending=False)
    sentiment_mean = df_sent['sentiment'].groupby(df_sent.index).mean().iloc[-190:-7]  # 3月1日-8月31日
    # y 轴
    y_bar = list(sentiment_mean)
    a = list(sentiment_mean.index)
    x_bar = []
    for i in a:
        term = str(i).split(" ")[0]
        x_bar.append(term)
    back_result = []
    for j in range(len(x_bar)):
        xy_set = (x_bar[j], y_bar[j])
        back_result.append(xy_set)
    list_list=[]
    for  xx  in  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        item={
            "class":xx/10,
            "Num": str(y[xx-1]),
            "Percent": str("{:0.2f}".format(y[xx-1]/count_y))
        }
        list_list.append(item)
    with open("./analysis/static/json/page4-3.json", "w", encoding='utf-8') as f:
        json.dump(list_list, f, ensure_ascii=False)
    context = {
        "pie": pie,
        "line": back_result,
        "x": ["情感倾向：0.1(最消极)", "情感倾向：0.2", "情感倾向：0.3", "情感倾向：0.4", "情感倾向：0.5", "情感倾向：0.6", "情感倾向：0.7", "情感倾向：0.8", "情感倾向：0.9", "情感倾向：1.0(最积极)"],
        "y": y,
        'x_bar': x_bar,
        'y_bar': y_bar
    }
    return render(request, 'page4_3.html', context)

def Contact_us(request):
    context = {
    }
    return render(request, 'contact_us.html', context)
