# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

count_pages = int(input())
pages_per_hour = int(input())
count_days = int(input())

hours_per_day = int(count_pages / pages_per_hour / count_days)
print(hours_per_day)
