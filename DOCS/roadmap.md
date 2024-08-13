# Future commands:


- ### -s, --show Status: Pending

**This command will display full information about
the current git repository for example things like a full
list of commits and a full list of files that are being
tracked or not plus their current status always keeping a clean
interface plus some really cool icons**

Some things that could be into the information displayed are:

- A list of the latest commits
- Blame for those commits
- Time for the commits
- Status of the repository
- All the files that are in the repository (plus their status)

among other important information abour the repository

- ### -p, --push Status: Pending

**A full optimization of the push process where the user
has to pretty much just commit and pygit should be able to complete
do the rest of the work for the user always keeping a clean user experience**

- ### setup subparcer Status: Being work on
**Util to setup pygit++ configuration. In the future this will lead
into a more complex customization system such as deciding what color is
each thing being displayed on**

- ### --init command Status: Being work on
**The definitive way to setup a dir that has some work already. [More docs coming soon]**



# DONE ✅

- ### -m, -man Status: Implemented ✅
**Display the DOCS locally!!**


- ### -G Status: Implemented ✅
**A way to pass git that haven't been implemented into pygit++ yet
for example now you can run ```pygit++ -G "restore foo.lua" -a```
really useful to make simpler pipelines.
**


- ### -a, -add Status: Implemented ✅
**A interactive way to add files to the index of the repo**


- ### -c, --commit Status: Implemented ✅ 
**A better way to commit your work for example now you can select
what is your commit about (for example you added something '[ADD]' 
or you modified somethings '[MODIFY]') and this will be added as a 
prefix to your commit automatically plus some other extra functions
such a counter that will tell when your commit is either too long 
or if you are just in the recommended size of a commit**
