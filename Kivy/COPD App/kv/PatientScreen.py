<PatientScreen>:
    BoxLayout:
        orientation: 'vertical'        
        halign: 'center'
        BoxLayout:
            size_hint_y: 0.2
            padding: 3
            Label:
                text: 'Patient Information'
                font_size: 50.
                halign: 'center'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                padding: 5
                BoxLayout:
                    size_hint_y: 0.1
                    padding: 5
                    Label:
                        text: 'Enter Patient Information'
                        font_size: 20.
                BoxLayout:
                    size_hint_y: 0.1
                    padding: 5
                    spacing: 10
                    Button:
                        text: 'New Patient'
                        on_press: root.new_patient()
                    Button:
                        text:'Existing Patient'
                        on_press: root.open_popup()
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: pid
                        text: 'Patient ID'
                    TextInput:
                        id: pid
                        multiline:False
                        text: root.patient_ID()
                    Button:
                        text: 'Find'
                        on_press: root.search_db()
                
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: fname_l
                        text: 'First Name:'
                    TextInput:
                        id: fname
                        multiline: False
                        text: 'Enter Name'
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: lname_l
                        text: 'Last Name:'
                    TextInput:
                        id: lname
                        text: 'Enter surname'
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: height_l
                        text: 'Height(cm):'
                    TextInput:
                        id: height
                        text: '1'
                    Label:
                        id: weight_l
                        text: 'Weight(kg):'
                    TextInput:
                        id: weight
                        text: '1'
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: gender
                        text: 'Gender:'
                    CheckBox:
                        id: male1
                        value: root.male
                        group: 'sex'                        
                    Label:
                        text: 'Male'
                        
                    CheckBox:
                        id: female1
                        value: root.female
                        group: 'sex'                        
                    Label:
                        text: 'Female'
                        
                    CheckBox:
                        id: mixed1
                        value: root.mixed
                        group: 'sex'                        
                    Label:
                        text: 'Other'
                        
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: dob_l
                        text: 'Date of Birth:'
                    TextInput:
                        id: dob
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Label:
                        id: smoker_l
                        text: 'Smoker:'
                    TextInput:
                        id: smoker
                BoxLayout:
                    size_hint_y: 0.1
                    spacing: 10.
                    padding: 5
                    Button:
                        id: ok
                        text: 'OK'                        
                        on_release: root.storevalue()
                    Button:
                        id: cancel
                        text: 'CANCEL'
#            FloatLayout:
#                orientation: 'vertical'
#                canvas:
#                    Rectangle:
#                        pos: 550,250
#                        source: 'C:\Users\VIRAL\.kivy\icon\kivy-icon-512.png'
        BoxLayout:
            size_hint_y: 0.1
            spacing: 25.
            padding: 2
            Button:
                text: 'Patient'
                on_press: root.manager.current = 'patient'
            Button:
                text: 'Spirometry'
                on_press: root.manager.current = 'spirometry'
            Button:
                text: 'Classification'
                on_press: root.manager.current = 'classification'
            Button:
                text: 'Treatment'
                on_press: root.manager.current = 'treatment'
            Button:
                text: 'Tutorial'
                on_press: root.manager.current = 'tutorial'
    BoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.2
            