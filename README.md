# Cashier Project

Ini merupakan GitHub Repository untuk Final Project course Python Pacmann.

## Background Project

Dalam project ini, diberikan skenario sebuah supermarket yang akan membuat sistem *cashier* yang *self-service*, sehingga *customer* bisa langsung memasukkan item, jumlah, dan harga yang dibeli. Fitur-fitur yang dibuat sebagai berikut:

1. Customer menambahkan item yang dibeli
    ```python
    add_item([<nama_item>, <jumlah_item>, <harga_item>])
    ```
2. Customer bisa cek detail barang yang diinput sudah benar.
    ```python
<<<<<<< HEAD
    check_order()
    ```
3. Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, customer bisa melakukan
    a. Update nama item
   ```python
   update_item_name([<old_name>, <new_name>])
   ```
    b. Update jumlah item
   ```python
   update_item_quantity([<item_name>, <new_qty>])
   ```
    c. Update harga item
   ```python
   update_item_price([<item_name>, <new_price>])
   ```
5. Jika batal membeli item belanjaan, customer bisa melakukan
    a. Menghapus salah satu item
   ```python
   delete_item([<item_name>])
   ```
    b. Langsung menghapus semua transaksi atau reset transaksi
   ```python
   reset_transaction()
   ```
6. Menghitung total belanja yang sudah dibeli. Sistem juga akan otomatis memberikan diskon dengan ketentuan harga minimum pembelian
=======
       check_order()
    ```
3. Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, customer bisa melakukan
    a. Update nama item
        ```python
        update_item_name([<old_name>, <new_name>])
        ```
    b. Update jumlah item
        ```python
        update_item_quantity([<item_name>, <new_qty>])
        ```
    c. Update harga item
        ```python
        update_item_price([<item_name>, <new_price>])
        ```
4. Jika batal membeli item belanjaan, customer bisa melakukan
    a. Menghapus salah satu item
        ```python
        delete_item([<item_name>])
        ```
    b. Langsung menghapus semua transaksi atau reset transaksi
        ```python
        reset_transaction()
        ```
5. Menghitung total belanja yang sudah dibeli. Sistem juga akan otomatis memberikan diskon dengan ketentuan harga minimum pembelian
>>>>>>> a56205844306922dc53a425db3da82712e3430b5
    ```python
       total_price()
    ```
    
## Alur Program (Flowchart)
![Flowchart](https://github.com/user-attachments/assets/cf148b8c-058d-497b-92c0-07fc89c47884)



## Hasil Test Case

1. Penambahan Item

```bash
<<<<<<< HEAD
PS F:\Talitha\Kuliah dan lain-lain\Pacmann.ai_Data Analyst Class\GIT\Final Project> python project_cashier.py
=======
PS F:\Talitha\Kuliah dan lain-lain\Pacmann.ai_Data Analyst Class\GIT> python project_cashier.py
>>>>>>> a56205844306922dc53a425db3da82712e3430b5
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 1
Input Item Name: Ayam
Input Item Quantity: 3
Input Item Price: 32000

Item successfully added!

Item Name: Ayam 
Quantity: 3
<<<<<<< HEAD
Price: Rp 32000.0
```

2. Menampilkan daftar item yang sudah ditambahkan
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 2
==================ORDER LIST==================
╒══════╤════════════════╤════════════╤══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │
╞══════╪════════════════╪════════════╪══════════════╡
│    1 │      Ayam      │          3 │        32000 │
├──────┼────────────────┼────────────┼──────────────┤
│    2 │     Banana     │          7 │        25000 │
├──────┼────────────────┼────────────┼──────────────┤
│    3 │  Tooth Paste   │          2 │        14500 │
├──────┼────────────────┼────────────┼──────────────┤
│    4 │    Shampoo     │          2 │        24000 │
├──────┼────────────────┼────────────┼──────────────┤
│    5 │ Instant Noodle │         10 │         3000 │
╘══════╧════════════════╧════════════╧══════════════╛
```

3. Mengoreksi input yang salah
    - Update nama
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 3
Specify the column you want to edit (*name/quantity/price):name
Write the wrong item name (*make sure the item name is correct):Ayam
Write the new item name:Chicken

Item has been updated!
==================ORDER LIST==================
╒══════╤════════════════╤════════════╤══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │
╞══════╪════════════════╪════════════╪══════════════╡
│    1 │     Banana     │          7 │        25000 │
├──────┼────────────────┼────────────┼──────────────┤
│    2 │  Tooth Paste   │          2 │        14500 │
├──────┼────────────────┼────────────┼──────────────┤
│    3 │    Shampoo     │          2 │        24000 │
├──────┼────────────────┼────────────┼──────────────┤
│    4 │ Instant Noodle │         10 │         3000 │
├──────┼────────────────┼────────────┼──────────────┤
│    5 │    Chicken     │          3 │        32000 │
╘══════╧════════════════╧════════════╧══════════════╛
```

    - Update quantity
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 3
Specify the column you want to edit (*name/quantity/price):quantity
Which item do you want to change?Instant Noodle
Enter new quantity:15

Item has been updated!
==================ORDER LIST==================
╒══════╤════════════════╤════════════╤══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │
╞══════╪════════════════╪════════════╪══════════════╡
│    1 │     Banana     │          7 │        25000 │
├──────┼────────────────┼────────────┼──────────────┤
│    2 │  Tooth Paste   │          2 │        14500 │
├──────┼────────────────┼────────────┼──────────────┤
│    3 │    Shampoo     │          2 │        24000 │
├──────┼────────────────┼────────────┼──────────────┤
│    4 │ Instant Noodle │         15 │         3000 │
├──────┼────────────────┼────────────┼──────────────┤
│    5 │    Chicken     │          3 │        32000 │
╘══════╧════════════════╧════════════╧══════════════╛
```

    - Update price
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 3
Specify the column you want to edit (*name/quantity/price):price
Which item do you want to change?Shampoo
Enter new price:25500

Item has been updated!
==================ORDER LIST==================
╒══════╤════════════════╤════════════╤══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │
╞══════╪════════════════╪════════════╪══════════════╡
│    1 │     Banana     │          7 │        25000 │
├──────┼────────────────┼────────────┼──────────────┤
│    2 │  Tooth Paste   │          2 │        14500 │
├──────┼────────────────┼────────────┼──────────────┤
│    3 │    Shampoo     │          2 │        25500 │
├──────┼────────────────┼────────────┼──────────────┤
│    4 │ Instant Noodle │         15 │         3000 │
├──────┼────────────────┼────────────┼──────────────┤
│    5 │    Chicken     │          3 │        32000 │
╘══════╧════════════════╧════════════╧══════════════╛
```

4. Menghapus item
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 4
Enter item name to delete: Tooth Paste
Item has successfully deleted!
==================ORDER LIST==================
╒══════╤════════════════╤════════════╤══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │
╞══════╪════════════════╪════════════╪══════════════╡
│    1 │     Banana     │          7 │        25000 │
├──────┼────────────────┼────────────┼──────────────┤
│    2 │    Shampoo     │          2 │        25500 │
├──────┼────────────────┼────────────┼──────────────┤
│    3 │ Instant Noodle │         15 │         3000 │
├──────┼────────────────┼────────────┼──────────────┤
│    4 │    Chicken     │          3 │        32000 │
╘══════╧════════════════╧════════════╧══════════════╛
```

5. Mencetak struk dan menghitung total harga
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 6
==================RECEIPT==================
╒══════╤════════════════╤════════════╤══════════════╤═══════════════╕
│   No │   Item Name    │   Item Qty │   Item Price │   Total Price │
╞══════╪════════════════╪════════════╪══════════════╪═══════════════╡
│    1 │     Banana     │          7 │        25000 │        175000 │
├──────┼────────────────┼────────────┼──────────────┼───────────────┤
│    2 │    Shampoo     │          2 │        25500 │         51000 │
├──────┼────────────────┼────────────┼──────────────┼───────────────┤
│    3 │ Instant Noodle │         15 │         3000 │         45000 │
├──────┼────────────────┼────────────┼──────────────┼───────────────┤
│    4 │    Chicken     │          3 │        32000 │         96000 │
╘══════╧════════════════╧════════════╧══════════════╧═══════════════╛
TOTAL PRICE: Rp 367,000.00
DISCOUNT: 8%
FINAL PRICE: Rp 337,640.00
```

6. Menghapus semua transaksi (reset transaksi)
```bash
------------------------------------------------------------
WELCOME TO PACMANN SUPERMARKET
------------------------------------------------------------
1. Add Items
2. Show list of Items
3. Update Items
4. Delete Items
5. Clear All Items
6. Print Receipt
7. Exit
------------------------------------------------------------

Enter Task Number : 5
All items successfully deleted!
```
=======
Price: 32000.0
```
>>>>>>> a56205844306922dc53a425db3da82712e3430b5
