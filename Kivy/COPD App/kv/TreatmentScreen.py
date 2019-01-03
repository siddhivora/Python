<TreatmentScreen>:
    BoxLayout:
        Label:
            text: 'Treatment'
        Button:
            text: 'Back to Patient'
            on_press: root.manager.current = 'patient'