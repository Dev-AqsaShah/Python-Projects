import numpy as np

# Task 1: 10 student marks array
marks = np.array([45.5, 78.0, 33.0, 91.5, 55.0, 62.5, 48.0, 85.0, 29.5, 70.0])

# Task 2: shape, size, dtype
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Dtype:", marks.dtype)

# Task 3: mean, median, highest, lowest, std
# average
print("\nMean:", np.mean(marks)) 

# beech wali value
print("Median:", np.median(marks))

# highest marks
print("Highest:", np.max(marks))

# lowest marks
print("Lowest:", np.min(marks))

# standerd deviation
print("Standard Deviation:", np.std(marks))


# Task 4: marks above mean
mean = np.mean(marks)
above_mean = marks[marks > mean]
print("\nAbove Average Students Marks:", above_mean)

# Task 5: replace marks below 50 with 50
marks[marks < 50] = 50
print("\nFinal Modified Array:", marks)
