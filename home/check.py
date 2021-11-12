from typing import Counter


def data_type_handling(data):
    for i in range(len(data)):
        data[i] = data[i]["fields"]
    return data

gus = [{"model": "home.soluongkhach", "pk": 110, "fields": {"guests": 118734, "inland": 116133, "foreignG": 2601, "month": "2021-04-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 111, "fields": {"guests": 107304, "inland": 104651, "foreignG": 2653, "month": "2021-03-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 112, "fields": {"guests": 110955, "inland": 108408, "foreignG": 2547, "month": "2021-02-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 113, "fields": {"guests": 112655, "inland": 110212, "foreignG": 2443, "month": "2021-01-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 114, "fields": {"guests": 77689, "inland": 75352, "foreignG": 2337, "month": "2020-12-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 115, "fields": {"guests": 71782, "inland": 69509, "foreignG": 2273, "month": "2020-11-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 116, "fields": {"guests": 75161, "inland": 72241, "foreignG": 2920, "month": "2020-10-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 117, "fields": {"guests": 67743, "inland": 64166, "foreignG": 3577, "month": "2020-09-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 118, "fields": {"guests": 194993, "inland": 188578, "foreignG": 6415, "month": "2020-08-01", "created_at": 0}}, {"model": "home.soluongkhach", "pk": 119, "fields": {"guests": 113638, "inland": 108298, "foreignG": 5340, "month": "2020-07-01", "created_at": 0}}]
gus = data_type_handling(gus)


