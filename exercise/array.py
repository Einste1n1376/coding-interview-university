class DynamicArray:
    def __init__(self, capacity=16):
        """初始化动态数组，默认容量为16"""
        if capacity < 0:
            raise ValueError("数组容量不能为负数")
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity
    
    def size(self):
        """返回数组中元素的数量"""
        return self._size
    
    def capacity(self):
        """返回数组的容量"""
        return self._capacity
    
    def is_empty(self):
        """判断数组是否为空"""
        return self._size == 0
    
    def at(self, index):
        """获取指定索引的元素"""
        self._check_index(index)
        return self._data[index]
    
    def push(self, item):
        """在数组末尾添加元素"""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = item
        self._size += 1
    
    def insert(self, index, item):
        """在指定索引插入元素"""
        if index < 0 or index > self._size:
            raise IndexError(f"索引超出范围: {index}")
        
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
            
        # 将插入位置后的元素向后移动
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
            
        self._data[index] = item
        self._size += 1
    
    def prepend(self, item):
        """在数组开头插入元素"""
        self.insert(0, item)
    
    def pop(self):
        """删除并返回末尾元素"""
        if self.is_empty():
            raise IndexError("数组为空，无法弹出元素")
        
        item = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        
        # 如果数组使用率不足25%，缩小容量
        if self._capacity > 16 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
            
        return item
    
    def delete(self, index):
        """删除指定索引的元素"""
        self._check_index(index)
        
        # 将删除位置后的元素向前移动
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
            
        self._data[self._size - 1] = None
        self._size -= 1
        
        # 如果数组使用率不足25%，缩小容量
        if self._capacity > 16 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
    
    def remove(self, item):
        """删除第一个匹配的元素"""
        for i in range(self._size):
            if self._data[i] == item:
                self.delete(i)
                return
        raise ValueError(f"未找到元素: {item}")
    
    def find(self, item):
        """查找元素并返回索引，未找到返回-1"""
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1
    
    def _resize(self, new_capacity):
        """调整数组容量"""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
    
    def _check_index(self, index):
        """检查索引是否有效"""
        if index < 0 or index >= self._size:
            raise IndexError(f"索引超出范围: {index}")
    
    def __str__(self):
        """返回数组的字符串表示"""
        return str([self._data[i] for i in range(self._size)])
    
    def __repr__(self):
        return self.__str__()


# 测试代码
if __name__ == "__main__":
    arr = DynamicArray(2)  # 创建初始容量为2的动态数组
    
    # 测试添加和自动扩容
    print("测试添加元素:")
    for i in range(5):
        arr.push(i)
        print(f"添加 {i}，数组: {arr}，大小: {arr.size()}，容量: {arr.capacity()}")
    
    # 测试获取
    print("\n测试获取元素:")
    for i in range(arr.size()):
        print(f"索引 {i} 的元素: {arr.at(i)}")
    
    # 测试插入
    print("\n测试插入元素:")
    arr.insert(2, 10)
    print(f"在索引2插入10后: {arr}")
    arr.prepend(20)
    print(f"在开头插入20后: {arr}")
    
    # 测试删除
    print("\n测试删除元素:")
    popped = arr.pop()
    print(f"弹出末尾元素 {popped}，数组: {arr}")
    arr.delete(1)
    print(f"删除索引1的元素后: {arr}")
    
    # 测试查找
    print("\n测试查找元素:")
    print(f"查找元素10的索引: {arr.find(10)}")
    print(f"查找元素100的索引: {arr.find(100)}")
