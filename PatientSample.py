import wx

def search(event): # searches for document
        
    try:
        global userInput
        userInput = fileName.GetValue()
        file = open(userInput)
        contents.SetValue(file.read())
        file.close()
    except(IOError):
        userInput = " "
        contents.SetValue("File is not existent")
        
def save(event): # modifies document
    try:
        file = open(userInput, 'w')
        file.write(contents.GetValue())
        file.close()
        contents.SetValue('%s has been modified' % (userInput))
    except(IOError):
        contents.SetValue("Please type another into the search bar.")
 
def newPatient(event):
    
    newGUI = PatientGUI()
    newGUI.PatientGUImaker()

class mainGUI:
    
    def mainGUImaker(self):

        global fileName
        global contents
        
        app = wx.App()
        win = wx.Frame(None, title="Patient Interface", size=(450, 300))

        bkg = wx.Panel(win)

        searchButton = wx.Button(bkg, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, search)

        modifyButton = wx.Button(bkg, label="Modify")
        modifyButton.Bind(wx.EVT_BUTTON, save)

        newPatientButton = wx.Button(bkg, label="Create New")
        newPatientButton.Bind(wx.EVT_BUTTON, newPatient)

        fileName = wx.TextCtrl(bkg)
        contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
        contents.SetValue("Thank you for using this program. To look for a existing patient file, type an existing \n patient file in the form John Smith.txt, and click the search button. If you want to \n modify a patient file, modify the text after searching for the text file and press \n modify when finished. If you wish to create a new patient file, press \n the create new button.")
        
        hbox = wx.BoxSizer()
        hbox.Add(fileName, proportion=1, flag=wx.EXPAND)
        hbox.Add(searchButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(modifyButton, proportion=0, flag=wx.LEFT, border=5)
        hbox.Add(newPatientButton, proportion=0, flag=wx.LEFT, border=5)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(contents, proportion=1,
        flag=wx.EXPAND | wx.LEFT | wx.LEFT | wx.LEFT, border=5)
        bkg.SetSizer(vbox)
        
        win.Show()
        app.MainLoop()
    
class PatientGUI:
    
    def PatientGUImaker(self): # code has not been modified yet
        
        app = wx.App()
        win = wx.Frame(None, title="New Patient Filing", size=(600, 330))

        bkg = wx.Panel(win)

        # Creating the static texts
        self.nameLabel = wx.StaticText(bkg, label ="Patient's Name:")
        self.birthLabel = wx.StaticText(bkg, label ="Birth Date:")
        self.SSLabel = wx.StaticText(bkg, label ="SS#:")
        self.singleLabel = wx.StaticText(bkg, label ="Single:")
        self.marryLabel = wx.StaticText(bkg, label ="Married:")
        self.streetLabel = wx.StaticText(bkg, label ="Street of Residence:")
        self.cityLabel = wx.StaticText(bkg, label ="City:")
        self.stateLabel = wx.StaticText(bkg, label ="State:")
        self.zipLabel = wx.StaticText(bkg, label ="Zip Code:")
        self.teleLabel = wx.StaticText(bkg, label ="Home Telephone:")
        self.employLabel = wx.StaticText(bkg, label ="Employer:")
        self.posLabel = wx.StaticText(bkg, label ="Position:")
        self.spouseLabel = wx.StaticText(bkg, label ="Spouse or Parent Name:")
        self.priLabel = wx.StaticText(bkg, label ="Primary Insurance:")
        self.polLabel1 = wx.StaticText(bkg, label ="Policy #:")
        self.groupLabel1 = wx.StaticText(bkg, label ="Group #:")
        self.secLabel = wx.StaticText(bkg, label ="Secondary Insurance:")
        self.polLabel2 = wx.StaticText(bkg, label ="Policy #:")
        self.groupLabel2 = wx.StaticText(bkg, label ="Group #:")
        self.mediLabel = wx.StaticText(bkg, label ="Current Medication:")
        self.alleLabel = wx.StaticText(bkg, label ="Allegies:")

        # Creating the CtrlTexts
        self.nameText = wx.TextCtrl(bkg)
        self.birthText = wx.TextCtrl(bkg)
        self.SSText = wx.TextCtrl(bkg)
        self.singleText = wx.TextCtrl(bkg)
        self.marryText = wx.TextCtrl(bkg)
        self.streetText = wx.TextCtrl(bkg)
        self.cityText = wx.TextCtrl(bkg)
        self.stateText = wx.TextCtrl(bkg)
        self.zipText = wx.TextCtrl(bkg)
        self.teleText = wx.TextCtrl(bkg)
        self.employText = wx.TextCtrl(bkg)
        self.posText = wx.TextCtrl(bkg)
        self.spouseText = wx.TextCtrl(bkg)
        self.priText = wx.TextCtrl(bkg)
        self.polText1 = wx.TextCtrl(bkg)
        self.groupText1 = wx.TextCtrl(bkg)
        self.secText = wx.TextCtrl(bkg)
        self.polText2 = wx.TextCtrl(bkg)
        self.groupText2 = wx.TextCtrl(bkg)
        self.mediText = wx.TextCtrl(bkg)
        self.alleText = wx.TextCtrl(bkg)

        # Creating the Buttons
        self.finishButton = wx.Button(bkg, label="Finish")
        self.finishButton.Bind(wx.EVT_BUTTON, self.finish)

        # Creating sizers
        box1 = wx.BoxSizer()
        box1.Add(self.nameLabel, proportion=0, flag=wx.LEFT, border=5)
        box1.Add(self.nameText, proportion=0, flag=wx.LEFT, border=5)
        box1.Add(self.birthLabel, proportion=0, flag=wx.LEFT, border=5)
        box1.Add(self.birthText, proportion=0, flag=wx.LEFT, border=5)
        box1.Add(self.SSLabel, proportion=0, flag=wx.LEFT, border=5)
        box1.Add(self.SSText, proportion=0, flag=wx.LEFT, border=5)

        box2 = wx.BoxSizer()
        box2.Add(self.singleLabel, proportion=0, flag=wx.LEFT, border=5)
        box2.Add(self.singleText, proportion=0, flag=wx.LEFT, border=5)
        box2.Add(self.marryLabel, proportion=0, flag=wx.LEFT, border=5)
        box2.Add(self.marryText, proportion=0, flag=wx.LEFT, border=5)
        box2.Add(self.streetLabel, proportion=0, flag=wx.LEFT, border=5)
        box2.Add(self.streetText, proportion=0, flag=wx.LEFT, border=5)

        box3 = wx.BoxSizer()
        box3.Add(self.cityLabel, proportion=0, flag=wx.LEFT, border=5)
        box3.Add(self.cityText, proportion=0, flag=wx.LEFT, border=5)
        box3.Add(self.stateLabel, proportion=0, flag=wx.LEFT, border=5)
        box3.Add(self.stateText, proportion=0, flag=wx.LEFT, border=5)
        box3.Add(self.zipLabel, proportion=0, flag=wx.LEFT, border=5)
        box3.Add(self.zipText, proportion=0, flag=wx.LEFT, border=5)

        box4 = wx.BoxSizer()
        box4.Add(self.teleLabel, proportion=0, flag=wx.LEFT, border=5)
        box4.Add(self.teleText, proportion=0, flag=wx.LEFT, border=5)
        box4.Add(self.employLabel, proportion=0, flag=wx.LEFT, border=5)
        box4.Add(self.employText, proportion=0, flag=wx.LEFT, border=5)
        box4.Add(self.posLabel, proportion=0, flag=wx.LEFT, border=5)
        box4.Add(self.posText, proportion=0, flag=wx.LEFT, border=5)

        box5 = wx.BoxSizer()
        box5.Add(self.spouseLabel, proportion=0, flag=wx.LEFT, border=5)
        box5.Add(self.spouseText, proportion=0, flag=wx.LEFT, border=5)

        box6 = wx.BoxSizer()
        box6.Add(self.priLabel, proportion=0, flag=wx.LEFT, border=5)
        box6.Add(self.priText, proportion=0, flag=wx.LEFT, border=5)
        box6.Add(self.polLabel1, proportion=0, flag=wx.LEFT, border=5)
        box6.Add(self.polText1, proportion=0, flag=wx.LEFT, border=5)
        box6.Add(self.groupLabel1, proportion=0, flag=wx.LEFT, border=5)
        box6.Add(self.groupText1, proportion=0, flag=wx.LEFT, border=5)

        box7 = wx.BoxSizer()
        box7.Add(self.secLabel, proportion=0, flag=wx.LEFT, border=5)
        box7.Add(self.secText, proportion=0, flag=wx.LEFT, border=5)
        box7.Add(self.polLabel2, proportion=0, flag=wx.LEFT, border=5)
        box7.Add(self.polText2, proportion=0, flag=wx.LEFT, border=5)
        box7.Add(self.groupLabel2, proportion=0, flag=wx.LEFT, border=5)
        box7.Add(self.groupText2, proportion=0, flag=wx.LEFT, border=5)
        
        box8 = wx.BoxSizer()
        box8.Add(self.mediLabel, proportion=0, flag=wx.LEFT, border=5)
        box8.Add(self.mediText, proportion=0, flag=wx.LEFT, border=5)
        box8.Add(self.alleLabel, proportion=0, flag=wx.LEFT, border=5)
        box8.Add(self.alleText, proportion=0, flag=wx.LEFT, border=5)

        final = wx.BoxSizer(wx.VERTICAL)
        final.Add(box1, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)        
        final.Add(box2, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box3, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box4, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box5, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box6, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box7, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(box8, proportion=0, flag=wx.BOTTOM | wx.TOP, border=5)
        final.Add(self.finishButton, proportion=1, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL , border=5)

        bkg.SetSizer(final)
                 
        win.Show()
        app.MainLoop()
        
    def finish(self, event):

        default = open("Patient_Template.txt")
        outputName = '%s%s' % (self.nameText.GetValue(), '.txt')
        output = open(outputName, 'w')
        info = [ ]
        info.append(self.nameText.GetValue())
        info.append(self.birthText.GetValue())
        info.append(self.SSText.GetValue())
        info.append(self.singleText.GetValue())
        info.append(self.marryText.GetValue())
        info.append(self.streetText.GetValue())
        info.append(self.cityText.GetValue())
        info.append(self.stateText.GetValue())
        info.append(self.zipText.GetValue())
        info.append(self.teleText.GetValue())
        info.append(self.employText.GetValue())
        info.append(self.posText.GetValue())
        info.append(self.spouseText.GetValue())
        info.append(self.priText.GetValue())
        info.append(self.polText1.GetValue())
        info.append(self.groupText1.GetValue())
        info.append(self.secText.GetValue())
        info.append(self.polText2.GetValue())
        info.append(self.groupText2.GetValue())
        info.append(self.mediText.GetValue())
        info.append(self.alleText.GetValue())
        
        for piece in info:
            temp = default.next().rstrip('\n')
            output.write('%s %s %s' % (temp, piece, '\n'))


        default.close()
        output.close()

        contents.SetValue("File Creation Complete!!")
        

newGUI = mainGUI()
newGUI.mainGUImaker()
    
