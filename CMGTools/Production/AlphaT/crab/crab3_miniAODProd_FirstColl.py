from WMCore.Configuration import Configuration

user    = "mbaber"
prodTag = "19Jun15"
sampleN = 1   
jobName = "GR_P_V56_Run2015A_PromptReco_v1"

datasets = ['/Jet/Run2015A-PromptReco-v1/AOD',
            '/HTMHT/Run2015A-PromptReco-v1/AOD'
            ]
labels   = ['Jet',
            'HTMHT'
            ]

dataset = datasets[ sampleN ]
label   = labels[ sampleN ]

config = Configuration()
config.section_('General')
config.General.workArea        = jobName + '_' + prodTag
config.General.transferOutputs = True
config.General.requestName     = label
config.section_('JobType')
config.JobType.psetName    = '../prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT.py'
config.JobType.pluginName  = 'Analysis'
config.JobType.outputFiles = ['prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT.root']
config.section_('Data')
config.Data.outLFNDirBase  = '/store/user/' + user + '/' + jobName + '_' + prodTag
config.Data.inputDBS       = 'global'
config.Data.inputDataset   = dataset
config.Data.publication    = False
config.Data.splitting      = 'FileBased'
config.Data.unitsPerJob    = 5
#config.Data.totalUnits     = 1
config.section_('User')
config.section_('Site')
config.Site.storageSite    = 'T2_UK_London_IC'
