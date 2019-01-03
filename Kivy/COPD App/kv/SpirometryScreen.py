<SpirometryScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 3
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.2
            padding: 1
            Label:
                text: 'Perform Test'
                font_size: 50
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.7
            padding: 5
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.2
                    padding: 7
                    Button:
                        text: 'Instructions'
#                        size_hint: 0.05, 0.05
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.15
                    padding: 5
                    spacing: 30
                    Button:
                        text: 'START'
#                        size_hint: 0.05, 0.05
                    Button:
                        text: 'RESTART'
#                        size_hint: 0.05, 0.05
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.7
                    padding: 5
#                    Graph:
#                        xlabel: 'Time'
#                        ylabel: 'Voltage'
#                        x_ticks_major: 25
#                        y_ticks_major: 1
#                        y_grid_label: True
#                        x_grid_label: True
#                        padding: 5
#                        x_grid: True
#                        y_grid: True
#                        xmin: -0
#                        xmax: 100
#                        ymin: -1
#                        ymax: 1
                        
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.15
                    padding: 5
                    Button:
                        text: 'SUBMIT'
#                        size_hint: 0.05, 0.05
            BoxLayout:
                orientation: 'vertical'
                padding: 5
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: 0.1
                    Label:
                        halign: 'left'
                        text_size: self.size
                        text: 'Respiratory Parameters:'                        
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.5
                    BoxLayout:
                        orientation: 'horizontal'
                        Label:
                            text: ''
                        Label:
                            text: 'Test Values'
                        Label:
                            text: 'Normal Range'
                    BoxLayout:
                        orientation: 'horizontal'
                        Label:
                            text: 'FEV1'
                        TextInput:
                            text: root.fev1_test()
                        TextInput:
                            text: root.fev1_predict()
                    BoxLayout:
                        orientation: 'horizontal'
                        Label:
                            text: 'FVC'
                        TextInput:
                            text: root.fvc_test()
                        TextInput:
                            text: root.fvc_predict()
                    BoxLayout:
                        orientation: 'horizontal'
                        Label:
                            text: 'FEV1/FVC'
                        TextInput:
                            id: fev1_fvc
                            text: root.fev1_fvc_test()
                        TextInput:
                            text: root.fev1_fvc_predict()
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: 0.3
                    BoxLayout:
                        orientation: 'horizontal'
                        Label:
                            text_size: self.size
                            halign: 'left'
                            text: 'COPD Diagnosis Result:'                                   
                    BoxLayout:
                        orientation: 'horizontal'
                        TextInput:
                            id: dresult
#                            text: root.diagnosis()
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 0.1
            padding: 10
            padding_top: 15
            spacing: 30
            Button:
                text: 'Back'
#                size_hint: 0.1, 0.1
                on_press: root.manager.current = 'patient'
            Button:
                text: 'Home'
#                size_hint: 0.1, 0.1
                on_press: root.manager.current = 'patient'
            Button:
                text: 'Next'
#                size_hint: 0.1, 0.1
                on_press: root.manager.current = 'classification'
        
        
#        BoxLayout:
#            orientation: 'vertical'
#            Button:
#                text: 'Start'
#                on_press: root.spiro_test()
#        BoxLayout:
#            orientation: 'vertical'
#        BoxLayout:
#            orientation: 'horizontal'
#            Label:
#                text: 'Spirometry'
#            Button:
#                text: 'Back to Patient'
#                on_press: root.manager.current = 'patient'