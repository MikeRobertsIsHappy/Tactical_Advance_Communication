
Google Cloud Deploy Instructions

Welcome to Clif 3 towls take 3 hours to dry in the sun, how long does it take 9 towles todry itect in this session is set to jacquelbot.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
mikerobertsishappy@cloudshell:~ (jacquelbot)$ git clone https://github.com/MikeRobertsIsHappy/jacquelbot_cloud
Cloning into 'jacquelbot_cloud'...
remote: Enumerating objects: 102, done.
remote: Counting objects: 100% (102/102), done.
remote: Compressing objects: 100% (78/78), done.
remote: Total 102 (delta 28), reused 88 (delta 18), pack-reused 0
Receiving objects: 100% (102/102), 4.48 MiB | 26.98 MiB/s, done.
Resolving deltas: 100% (28/28), done.
mikerobertsishappy@cloudshell:~ (jacquelbot)$ ls
jacquelbot_cloud  NeedsGameApp  README-cloudshell.txt
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd NeedGameApp
-bash: cd: NeedGameApp: No such file or directory
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd needsgameapp
-bash: cd: needsgameapp: No such file or directory
mikerobertsishappy@cloudshell:~ (jacquelbot)$ cd NeedsGameApp
mikerobertsishappy@cloudshell:~/NeedsGameApp (jacquelbot)$ gcloud init
Welcome! This command will take you through the configuration of gcloud.

Settings from your current configuration [cloudshell-7861] are:
accessibility:
  screen_reader: 'True'
component_manager:
  disable_update_check: 'True'
compute:
  gce_metadata_read_timeout_sec: '30'
core:
  account: mikerobertsishappy@gmail.com
  disable_usage_reporting: 'True'
  project: jacquelbot
metrics:
  environment: devshell

Pick configuration to use:
 [1] Re-initialize this configuration [cloudshell-7861] with new settings
 [2] Create a new configuration
Please enter your numeric choice:  1

Your current configuration has been set to: [cloudshell-7861]

You can skip diagnostics next time by using the following flag:
  gcloud init --skip-diagnostics

Network diagnostic detects and fixes local network connection issues.
Checking network connection...done.
Reachability Check passed.
Network diagnostic passed (1/1 checks passed).

Choose the account you would like to use to perform operations for this configuration:
 [1] mikerobertsishappy@gmail.com
 [2] Log in with a new account
Please enter your numeric choice:  1

You are logged in as: [mikerobertsishappy@gmail.com].

Pick cloud project to use:
 [1] jacquelbot
 [2] the-needs-game
 [3] Create a new project
Please enter numeric choice or text value (must exactly match list item):  2

Your current project has been set to: [the-needs-game].

Do you want to configure a default Compute Region and Zone? (Y/n)?  Y

Which Google Compute Engine zone would you like to use as project default?
If you do not specify a zone via a command line flag while working with Compute Engine resources, the default is assumed.
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] asia-east2-a
 [45] asia-east2-b
 [46] asia-east2-c
 [47] asia-northeast2-a
 [48] asia-northeast2-b
 [49] asia-northeast2-c
 [50] asia-northeast3-a
Did not print [39] options.
Too many options [89]. Enter "list" at prompt to print choices fully.
Please enter numeric choice or text value (must exactly match list item):  8

Your project default Compute Engine zone has been set to [us-central1-a].
You can change it by running [gcloud config set compute/zone NAME].

Your project default Compute Engine region has been set to [us-central1].
You can change it by running [gcloud config set compute/region NAME].

Your Google Cloud SDK is configured and ready to use!

* Commands that require authentication will use mikerobertsishappy@gmail.com by default
* Commands will reference project `the-needs-game` by default
* Compute Engine commands will use region `us-central1` by default
* Compute Engine commands will use zone `us-central1-a` by default

Run `gcloud help config` to learn how to change individual settings

This gcloud configuration is called [cloudshell-7861]. You can create additional configurations if you work with multiple accounts and/or projects.
Run `gcloud topic configurations` to learn more.

Some things to try next:

* Run `gcloud --help` to see the Cloud Platform services you can interact with. And run `gcloud help COMMAND` to get help on any gcloud command.
* Run `gcloud topic --help` to learn about advanced features of the SDK like arg files and output formatting
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
ERROR: (gcloud.app.deploy) Unable to deploy to application [the-needs-game] with status [USER_DISABLED]: Deploying to stopped apps is not allowed.
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ ^C
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$ gcloud app deploy
ERROR: (gcloud.app.deploy) Unable to deploy to application [the-needs-game] with status [USER_DISABLED]: Deploying to stopped apps is not allowed.
mikerobertsishappy@cloudshell:~/NeedsGameApp (the-needs-game)$