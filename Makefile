
#foreach d (`cat merge-sets/jobs_hadd.dtags.large_ab`)
#foreach d (`cat merge-sets/jobs_hadd.dtags.large_aa`)
#foreach d (`cat merge-sets/tt-sys/updowns.dtags`)
# merge-sets/jobs_hadd.dtags.single-muon
# merge-sets/jobs_hadd.dtags.single-electron

#echo foo & \
#


resubmit:
	for js in `ls crab_projects/crab_Ntupler_${nt}* -d`; \
	do \
	echo $$js ; \
	crab resubmit -d $$js ; \
	done


status:
	for js in `ls crab_projects/crab_Ntupler_${nt}* -d`; \
	do \
	echo $$js ; \
	crab status -d $$js ; \
	done


