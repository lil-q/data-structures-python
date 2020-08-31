public class MyHashMap<K,V> {

    // 最大容量，即桶数组 table 的大小
    int capacity;

    // 当前 key-value 条目数
    int size = 0;

    // 负载因子，当 size >= table * loadFactor 时，扩容
    final float loadFactor;

    // 桶数组，存放 Entry 链表
    Entry<K,V>[] table;

    // 键值对 Entry，格外保存 hash 和 next
    static class Entry<K,V> {
        final int hash;
        final K key;
        V value;
        Entry<K, V> next;

        Entry(int hash, K key, V value) {
            this.hash = hash;
            this.key = key;
            this.value = value;
        }
    }

    // 求 hash，对 Object 方法 HashCode() 得到的 hashcode 上下 16 位异或
    // 因为后续求桶下标实际上可能不会用到全部 hashcode，将高位异或到低位可以增加离散度
    static int hash(Object key) {
        int h = key.hashCode();
        return h ^ (h >>> 16);
    }

    public MyHashMap() {
        capacity = 16;
        loadFactor = 0.75f;
        table = new Entry[capacity];
    }

    public V get(Object key) {
        return getEntry(hash(key), key);
    }

    private V getEntry(int hash, Object key) {
        int index = hash & (capacity - 1);
        Entry<K,V> curr = table[index];
        while (curr != null) {
            if (curr.key.equals(key)) {
                return curr.value;
            }
            curr = curr.next;
        }
        return null;
    }

    public void put(K key, V value) {
        if (size >= capacity * loadFactor) {
            resize();
        }
        size++;
        putVal(hash(key), key, value);
        System.out.println("put key: " + key + "  value: " + value);
    }

    private void putVal(int hash, K key, V value) {
        int index = hash & (capacity - 1);
        if (table[index] == null) {
            table[index] = new Entry<>(hash, key, value);
        } else {
            Entry<K, V> curr = table[index], prev = null;
            while (curr != null && !curr.key.equals(key)) {
                prev = curr;
                curr = curr.next;
            }
            if (curr == null) {
                prev.next = new Entry<>(hash, key, value);
            } else {
                curr.value = value;
            }
        }
    }

    private void resize() {
        System.out.println("************************");
        System.out.println("resizing! " + capacity + " -> " + (capacity << 1));
        System.out.println("************************");
        capacity <<= 1;
        Entry<K,V>[] oldTable = table;
        table = new Entry[capacity];
        for (Entry entry : oldTable) {
            if (entry == null) continue;
            Entry curr = entry;
            while (curr != null) {
                // 注意到调用的是 putVal，这不会增加 size 的计数
                putVal(entry.hash, (K)entry.key, (V)entry.value);
                curr = curr.next;
            }
        }
    }

    public static void main(String[] args) {
        MyHashMap<Integer, String> map = new MyHashMap<>();
        for (int i = 100; i < 120; i++) {
            map.put(i, "v" + i);
        }
        map.put(110, "newValue");
        System.out.println("\n");
        for (int i = 100; i < 120; i++) {
            System.out.println("get key: " + i + "  value: " + map.get(i));
        }
    }
}
