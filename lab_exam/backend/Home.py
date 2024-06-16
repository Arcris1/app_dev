from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
Form, Window = uic.loadUiType("frontend/home_page.ui")
from backend.db import Users, lastUserId, Items

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Form()
        self.ui.setupUi(self)
        
         # Set column headers
        self.ui.product_list.setColumnCount(4)
        self.ui.product_list.setHorizontalHeaderLabels(['Name', 'Category', 'Price', 'Quantity'])
        
        self.ui.product_list_2.setColumnCount(4)
        self.ui.product_list_2.setHorizontalHeaderLabels(['Name', 'Category', 'Quantity', 'Total Price'])
        
        # Connect item selection changed signal to method
        self.ui.product_list.itemSelectionChanged.connect(self.show_item_details)
        
        # Add item to selected list
        self.ui.add_item_btn.clicked.connect(self.add_item)
        
        # Add item to selected list
        self.ui.proceed_btn.clicked.connect(self.proceed)

        # Populate table with all items initially
        self.populate_table()
    
    def populate_table(self):
        self.ui.product_list.setRowCount(len(Items))
        
         # Iterate over the Items dictionary and populate the table
        for row, (key, item) in enumerate(Items.items()):
            self.ui.product_list.setItem(row, 0, QTableWidgetItem(item['name']))
            self.ui.product_list.setItem(row, 1, QTableWidgetItem(item['category']))
            self.ui.product_list.setItem(row, 2, QTableWidgetItem(f"{item['price']:.2f}"))
            self.ui.product_list.setItem(row, 3, QTableWidgetItem(str(item['quantity'])))

    def show_item_details(self):
        selected_items = self.ui.product_list.selectedItems()
        if len(selected_items) == 0:
            self.ui.item_name.setText("No item selected")
        else:
            self.selected_row = selected_items[0].row()
            self.selected_item_name = self.ui.product_list.item(self.selected_row, 0).text()
            self.selected_item_category = self.ui.product_list.item(self.selected_row, 1).text()
            self.selected_item_price = self.ui.product_list.item(self.selected_row, 2).text()
            self.selected_item_quantity = self.ui.product_list.item(self.selected_row, 3).text()

            self.ui.item_name.setText(self.selected_item_name)
            self.ui.price.setText(self.selected_item_price)
            
    def add_item(self):
         # Get selected item details from product_list
        selected_items = self.ui.product_list.selectedItems()
        
        if not selected_items:
            QMessageBox.warning(self, "No Item Selected", "Please select an item to add.")
            return
        
        qty_str = self.ui.qty.text().strip() 
        qty = int(qty_str) if qty_str else 1 
        total_price = qty * float(self.selected_item_price)
        
        if len(selected_items) == 0:
            QMessageBox.warning(self, "No Item Selected", "Please select an item to add.")
            return
        
         # Check if quantity is valid
        try:
            qty = int(self.ui.qty.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Quantity", "Please enter a valid quantity.")
            return
        
        if qty <= 0:
            QMessageBox.warning(self, "Invalid Quantity", "Quantity must be greater than zero.")
            return
        
        if not self.selected_item_name:
            QMessageBox.warning(self, "No item selected", "Please select an item before adding it.")
            return
        
        # Check if selected quantity is available
        if qty > int(self.selected_item_quantity):
            QMessageBox.warning(self, "Insufficient Quantity", f"Only {self.selected_item_quantity} available.")
            return
        
        # Add item to product_list_2
        row_position = self.ui.product_list_2.rowCount()
        self.ui.product_list_2.insertRow(row_position)
        self.ui.product_list_2.setItem(row_position, 0, QTableWidgetItem(self.selected_item_name))
        self.ui.product_list_2.setItem(row_position, 1, QTableWidgetItem(self.selected_item_category))
        self.ui.product_list_2.setItem(row_position, 2, QTableWidgetItem(str(qty)))
        self.ui.product_list_2.setItem(row_position, 3, QTableWidgetItem(f"${total_price}"))
        
        # Update product_list to reflect deducted quantity
        self.ui.product_list.setItem(self.selected_row, 3, QTableWidgetItem(str(int(self.selected_item_quantity) - qty)))

        self.calculate_total_price()
        
        self.ui.item_name.setText("")
        self.ui.price.setText("")
        self.ui.qty.setText("")
        
    def calculate_total_price(self):
        total_price = 0.0
        row_count = self.ui.product_list_2.rowCount()
        
        for row in range(row_count):
            total_price += float(self.ui.product_list_2.item(row, 3).text().replace('$', ''))
        
        self.ui.sub_total.setText(f"${total_price}")
        self.ui.total_amount.setText(f"${total_price}")
    
    def proceed(self):
        QMessageBox.information(self, "Successful", "Transaction Complete.")
        self.ui.sub_total.setText("$0.00")
        self.ui.total_amount.setText("$0.00")
        self.ui.item_name.setText("")
        self.ui.price.setText("")
        self.ui.qty.setText("")
        
        # Clear product_list_2
        self.ui.product_list_2.clearContents()
        self.ui.product_list_2.setRowCount(0) 
        