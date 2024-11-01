def enrollment_stats(universities: list):
    enrollments = []
    tuitions = []
    for uni in universities:
        enrollments.append(uni[1])
        tuitions.append(uni[2])
    return enrollments, tuitions

def mean(lists:list):
    if len(lists)>0:
        return sum(lists)/len(lists)
    else:
        return 0

def median(lists:list):
    count = len(lists)
    if count > 0:
        if count % 2 == 0:
            return (sorted(lists)[count // 2] + sorted(lists)[count // 2 + 1])
        else:
            return (sorted(lists)[count // 2])
    else:
        return 0


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments, tuitions = enrollment_stats (universities)
sumTuitions = sum (tuitions)
sumEnroll = sum (enrollments)

medianTuitions = median (tuitions)
medianEnroll = median (enrollments)

meanTuitions = mean (tuitions)
meanEnroll = mean (enrollments)

breaker = "******************************"

print(breaker)

print (f"Total students: {sumEnroll}")
print (f"Total tuition: $ {sumTuitions}\n")

print (f"Student mean: {meanEnroll:,.2f}")
print (f"Student median: {medianTuitions}\n")

print (f"Tuitions mean: $ {meanTuitions:,.2f}")
print (f"Tuitions median: $ {medianTuitions}")

print(breaker)
