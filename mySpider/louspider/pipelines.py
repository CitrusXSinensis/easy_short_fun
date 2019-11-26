# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LouPipeline(object):
    def process_item(self, item, spider):
        with open('courses.txt', 'a') as file:
            line = u"course_name: {0}, learned-count: {1}, image {2}\n".format(item['name'], item['learned'], item['image'])
            file.write(line)
        return item
