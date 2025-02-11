from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QLineEdit, QFileDialog, QTextEdit, QComboBox, QProgressBar, QFrame
)
from PyQt6.QtCore import Qt
QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
QLineEdit, QFileDialog, QTextEdit, QComboBox, QProgressBar, QFrame

import sys

class MainApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAD Request Submission")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        #layout.setSpacing(1)  # Reduce vertical spacing between widgets

        
        basic_prompt_label = QLabel("Basic Prompt")
        basic_prompt_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        
        self.basic_prompt = QTextEdit(self)
        self.basic_prompt.setPlaceholderText("Enter design request...")
        self.basic_prompt.setFixedHeight(40)  # Approx. 2 rows high initially
        self.basic_prompt.textChanged.connect(self.adjust_textedit_height)
        
        row_layout = QHBoxLayout()
        row_layout.addWidget(basic_prompt_label)
        row_layout.addWidget(self.basic_prompt)
        layout.addLayout(row_layout)
        



        


        
        # Advanced Section (Hidden by default)
        self.advanced_section = QFrame(self)
        self.advanced_section.setVisible(False)
        advanced_layout = QVBoxLayout()
        
        self.advanced_prompt = QTextEdit(self)
        self.advanced_prompt.setPlaceholderText("Enter design request...")
        
        self.coordinate_label = QLabel("Coordinate System")
        self.coord_system = QComboBox()
        self.coord_system.addItems(["Local Grid", "World Coordinate"])  
        
        # Local Grid System Inputs
        self.datum_input = QLineEdit(self)
        self.datum_input.setPlaceholderText("Datum")
        self.northing_input = QLineEdit(self)
        self.northing_input.setPlaceholderText("Northing & Easting bearings")
        
        # World Coordinate System Inputs
        self.world_system_input = QLineEdit(self)
        self.world_system_input.setPlaceholderText("System")
        self.zone_input = QLineEdit(self)
        self.zone_input.setPlaceholderText("Zone")
        
        # File Upload Sections
        self.survey_button = QPushButton("Upload Survey")
        self.survey_button.clicked.connect(self.upload_file)
        self.autocad_button = QPushButton("Upload AutoCAD Template")
        self.autocad_button.clicked.connect(self.upload_file)
        self.project_req_button = QPushButton("Upload Project Requirements")
        self.project_req_button.clicked.connect(self.upload_file)
        
        # Building Code
        self.building_code_input = QLineEdit(self)
        self.building_code_input.setPlaceholderText("Enter building code...")
        
        # Submit Button and Loading Indicator
        self.submit_button = QPushButton("Submit")
        self.loading_bar = QProgressBar(self)
        self.loading_bar.setVisible(False)
        
        # Toggle Button for Advanced Section
        self.toggle_advanced_button = QPushButton("Show Advanced Options")
        self.toggle_advanced_button.clicked.connect(self.toggle_advanced_section)
        
        advanced_layout.addWidget(QLabel("Advanced Prompt"))
        advanced_layout.addWidget(self.advanced_prompt)
        advanced_layout.addWidget(self.coordinate_label)
        advanced_layout.addWidget(self.coord_system)
        advanced_layout.addWidget(QLabel("Datum"))
        advanced_layout.addWidget(self.datum_input)
        advanced_layout.addWidget(QLabel("Northing & Easting"))
        advanced_layout.addWidget(self.northing_input)
        advanced_layout.addWidget(QLabel("World Coordinate System"))
        advanced_layout.addWidget(self.world_system_input)
        advanced_layout.addWidget(QLabel("Zone"))
        advanced_layout.addWidget(self.zone_input)
        advanced_layout.addWidget(self.survey_button)
        advanced_layout.addWidget(self.autocad_button)
        advanced_layout.addWidget(self.project_req_button)
        advanced_layout.addWidget(QLabel("Building Code"))
        advanced_layout.addWidget(self.building_code_input)
        advanced_layout.addWidget(self.submit_button)
        advanced_layout.addWidget(self.loading_bar)
        
        self.advanced_section.setLayout(advanced_layout)
        
        layout.addWidget(self.toggle_advanced_button)
        layout.addWidget(self.advanced_section)
        
        self.setLayout(layout)
    
    def toggle_advanced_section(self):
        if self.advanced_section.isVisible():
            self.advanced_section.setVisible(False)
            self.toggle_advanced_button.setText("Show Advanced Options")
        else:
            self.advanced_section.setVisible(True)
            self.toggle_advanced_button.setText("Hide Advanced Options")
    
    def adjust_textedit_height(self):
        document = self.basic_prompt.document()
        document.setTextWidth(self.basic_prompt.viewport().width())
        new_height = min(120, int(document.size().height()) + 10)  # Max height for 6 rows
        self.basic_prompt.setFixedHeight(new_height)
    
    def upload_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            print(f"File selected: {file_path}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
