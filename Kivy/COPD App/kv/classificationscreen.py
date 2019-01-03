<ClassificationScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.2
            Label:
                font_size: 50
                text: 'Classification'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.7
#            Ball:
#                id: bal_1
#            Ball:
#                id: bal_2
#            Ball:
#                id: bal_3
#            Ball:
#                id: bal_4
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.1
            padding: 10
            padding_top: 15
            spacing: 30
            Button:
                text: 'Back'
                on_press: root.manager.current = 'spirometry'
            Button:
                text: 'Home'
                on_press: root.manager.current = 'patient'
            Button:
                text: 'Next'
                on_press: root.manager.current = 'treatment'
