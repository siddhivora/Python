<exist_patient>:
    BoxLayout:
        size_hint_y: 0.1
        spacing: 10.
        padding: 5
        Label:
            id: pid
            text: '111111'
        TextInput:
            id: pid
            multiline:False
            text: 'Enter ID'
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
        ToggleButton:
            id: btn1
            text: 'Male'
            group: 'sex'
                                        
        ToggleButton:
            text: 'Female'
            group: 'sex'
            state: 'down'
            
        ToggleButton:
            text: 'Mixed'
            group: 'sex'
            
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
    