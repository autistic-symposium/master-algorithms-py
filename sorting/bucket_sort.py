#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def bucket_sort(list):

        buckets = [[] for _ in range(K)]

        shift = min(lst)
        max_val = max(lst) - shift
        bucket_size = max(1, max_val / K)

        for i, elem in enumerate(lst):

            index = (elem - shift) // bucket_size

            if index == K:
                buckets[K - 1].append(elem)
            else:
                buckets[index].append(elem)

        for bucket in buckets:
            bucket.sort()

        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(bucket)

        for i in range(len(lst)):
            lst[i] = sorted_array[i]
