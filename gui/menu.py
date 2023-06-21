"""
        fun1_action = QAction("Fun 1", self)
        fun2_action = QAction("Fun 2", self)
        fun3_action = QAction("Fun 3", self)

        # Подключаем действия к соответствующим функциям
        fun1_action.triggered.connect(self.translate_text)
        fun2_action.triggered.connect(self.open_wikipedia)
        fun3_action.triggered.connect(self.add_quote)

        # Создаем контекстное меню
        self.context_menu = QMenu(self)
        self.context_menu.addAction(fun1_action)
        self.context_menu.addAction(fun2_action)
        self.context_menu.addAction(fun3_action)

        # Создаем вертикальное расположение виджета
        layout = QVBoxLayout(self)

        # Создаем метку для отображения текста
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # Добавляем метку в вертикальное расположение
        layout.addWidget(self.label)

        # Устанавливаем контекстное меню для виджета
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)

    def open_context_menu(self, pos):
        # Показываем контекстное меню в позиции курсора
        self.context_menu.exec_(self.mapToGlobal(pos))

    def copy_text(self):
        self.label.setText("Copy")
        selected_text = self.ui_page.textEdit.textCursor().selectedText()


    def translate_text(self):
        self.label.setText("Translate")
        selected_text = self.ui_page.textEdit.textCursor().selectedText()
        translation = phrase_translation.PhraseTranslation.get_translation(selected_text)



    def open_wikipedia(self):
        self.label.setText("Wikipedia")
        selected_text = self.ui_page.textEdit.textCursor().selectedText()
        wikipedia_search.WikipediaSearch().search(selected_text)

    def add_quote(self):
        self.label.setText("Add quote")
        selected_text=self.ui_page.textEdit.textCursor().selectedText()
"""