#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bucket_sort(array, k):

        buckets = [[] for _ in range(k)]

        shift = min(array)
        max_val = max(array) - shift
        bucket_size = max(1, max_val / k)

        for i, e in enumerate(array):

            index = (e - shift) // bucket_size

            if index == k:
                buckets[k - 1].append(e)
            else:
                buckets[index].append(e)

        for bucket in buckets:
            bucket.sort()

        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(bucket)

        for i in range(len(array)):
            array[i] = sorted_array[i]
