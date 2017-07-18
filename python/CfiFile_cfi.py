import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('NtuplerAnalyzer',
           minTracks = cms.untracked.uint32(0)
)

ntupler = cms.EDAnalyzer('NtuplerAnalyzer',
    isMC = cms.untracked.bool(False),
    muHLT_MC1   = cms.string("HLT_IsoMu24_v4"  ),
    muHLT_MC2   = cms.string("HLT_IsoTkMu24_v4"),
    muHLT_Data1 = cms.string("HLT_IsoMu24_v*"  ),
    muHLT_Data2 = cms.string("HLT_IsoTkMu24_v*"),
    elHLT_Data  = cms.string("HLT_Ele27_WPTight_Gsf_v*"),
    elHLT_MC    = cms.string("HLT_Ele27_WPTight_Gsf_v7"),
    jecDir          = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/'),
    resolutionFile  = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/Spring16_25nsV10_MC_PtResolution_AK4PFchs.txt'),
    scaleFactorFile = cms.string('${CMSSW_BASE}/src/UserCode/ttbar-leptons-80X/data/jec/25ns/Spring16_25nsV10_MC_SF_AK4PFchs.txt'),

    jet_kino_cuts_pt  = cms.double( 30.),
    jet_kino_cuts_eta = cms.double( 2.4),
    tau_kino_cuts_pt  = cms.double( 30.),
    tau_kino_cuts_eta = cms.double( 2.3)
)

