
    gcloud compute instances create instance-1 ^
        --project=oca-infra-xp-lab ^
        --image-family=rhel-8 ^
        --image-project=rhel-cloud ^
        --machine-type=e2-medium ^
        --zone=europe-west9-a ^
        --network-interface=network=lab-test-project,stack-type=IPV4_ONLY,subnet=back,no-address ^
        --shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring 
