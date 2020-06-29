from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets

"""
1.手写体数字，监督学习
样本集：一批手写数字的图片，带标签（0--9）,10类
样本数据量为1797， 保存在sklearn的datesets里
每一个数据样本是由image,target两部分组成的
image是一个尺寸为8*8的图像（手写的数字0-9）
target是图像的类别（数字0-9）
2.划分训练集和测试集
3.选一个算法，构建一个模型 KNN
4.训练模型
5.预测，验证
"""
sample_data = datasets.load_digits()
images = sample_data.data
labels = sample_data.target
# 划分训练集和测试集
train_data， test_data, train_labels, test_labels = train_test_split(images,lables,test_size=01)
# 选择模型
model_knn = KNeighborsClassifier(n_neighbors=4, algorithm='auto',weights='distance')
#训练模型
model_knn.fit(train_data, train_labels)
# 预测，验证
pred = model_knn.predict(test_data)

print("pred: \n", pred)
print("test_labels:\n", test_labels)

# 查看准确率
acc = accuracy_score(pred, test_labels)
print("Accuracy rate:%.3f" % acc)