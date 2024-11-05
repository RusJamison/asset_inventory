![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Rusakaniko Jamison,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!


<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">97%</span>
        </h1>
    </div>
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th id="file" class="name left" aria-sort="none" data-shortcut="f">File<span class="arrows"></span></th>
                <th id="statements" aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements<span class="arrows"></span></th>
                <th id="missing" aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing<span class="arrows"></span></th>
                <th id="excluded" aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded<span class="arrows"></span></th>
                <th id="coverage" class="right" aria-sort="none" data-shortcut="c">coverage<span class="arrows"></span></th>
            </tr>
        </thead>
        <tbody>
            <tr class="region">
                <td class="name left"><a href="z_57760688d1f824db___init___py.html">core/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_57760688d1f824db_settings_py.html">core/settings.py</a></td>
                <td>36</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="36 36">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_57760688d1f824db_urls_py.html">core/urls.py</a></td>
                <td>8</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="7 8">88%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="env_py.html">env.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936___init___py.html">equipment/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_admin_py.html">equipment/admin.py</a></td>
                <td>15</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="15 15">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_apps_py.html">equipment/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_forms_py.html">equipment/forms.py</a></td>
                <td>22</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="22 22">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb_0001_initial_py.html">equipment/migrations/0001_initial.py</a></td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="6 6">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb_0002_alter_equipment_image_alter_equipment_user_manual_py.html">equipment/migrations/0002_alter_equipment_image_alter_equipment_user_manual.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb_0003_remove_equipment_health_facility_equipmentlocation_and_more_py.html">equipment/migrations/0003_remove_equipment_health_facility_equipmentlocation_and_more.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb_0004_alter_equipment_location_py.html">equipment/migrations/0004_alter_equipment_location.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb_0005_alter_equipment_image_alter_equipment_notes_and_more_py.html">equipment/migrations/0005_alter_equipment_image_alter_equipment_notes_and_more.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_88604d44b496bcbb___init___py.html">equipment/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_models_py.html">equipment/models.py</a></td>
                <td>81</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="80 81">99%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959___init___py.html">equipment/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959_test_create_py.html">equipment/tests/test_create.py</a></td>
                <td>36</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="36 36">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959_test_delete_py.html">equipment/tests/test_delete.py</a></td>
                <td>27</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="27 27">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959_test_details_py.html">equipment/tests/test_details.py</a></td>
                <td>30</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="30 30">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959_test_equipment_list_py.html">equipment/tests/test_equipment_list.py</a></td>
                <td>32</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="32 32">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_1ba715d6592ce959_test_update_py.html">equipment/tests/test_update.py</a></td>
                <td>34</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="34 34">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_urls_py.html">equipment/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_utils_py.html">equipment/utils.py</a></td>
                <td>7</td>
                <td>3</td>
                <td>0</td>
                <td class="right" data-ratio="4 7">57%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_4d6b1bc0a02fa936_views_py.html">equipment/views.py</a></td>
                <td>86</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="75 86">87%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="manage_py.html">manage.py</a></td>
                <td>11</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="9 11">82%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51___init___py.html">work_orders/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_admin_py.html">work_orders/admin.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_apps_py.html">work_orders/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_forms_py.html">work_orders/forms.py</a></td>
                <td>19</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="19 19">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097_0001_initial_py.html">work_orders/migrations/0001_initial.py</a></td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="6 6">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097_0002_alter_unscheduledworkorder_work_order_report_py.html">work_orders/migrations/0002_alter_unscheduledworkorder_work_order_report.py</a></td>
                <td>5</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="5 5">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097_0003_remove_scheduledworkorder_frequency_and_more_py.html">work_orders/migrations/0003_remove_scheduledworkorder_frequency_and_more.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097_0004_alter_unscheduledworkorder_status_py.html">work_orders/migrations/0004_alter_unscheduledworkorder_status.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097_0005_alter_unscheduledworkorder_closed_at_and_more_py.html">work_orders/migrations/0005_alter_unscheduledworkorder_closed_at_and_more.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_8d7ab8a156d2f097___init___py.html">work_orders/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_models_py.html">work_orders/models.py</a></td>
                <td>45</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="43 45">96%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_e84e7565cc1db528___init___py.html">work_orders/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_327a3c517aa378fb___init___py.html">work_orders/tests/scheduled/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_327a3c517aa378fb_test_create_py.html">work_orders/tests/scheduled/test_create.py</a></td>
                <td>33</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="33 33">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_327a3c517aa378fb_test_list_py.html">work_orders/tests/scheduled/test_list.py</a></td>
                <td>28</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="28 28">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_b02d463796305c53___init___py.html">work_orders/tests/unscheduled/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_b02d463796305c53_test_create_py.html">work_orders/tests/unscheduled/test_create.py</a></td>
                <td>36</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="36 36">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_b02d463796305c53_test_list_py.html">work_orders/tests/unscheduled/test_list.py</a></td>
                <td>31</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="31 31">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_urls_py.html">work_orders/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="region">
                <td class="name left"><a href="z_2181fedf9a8cec51_views_py.html">work_orders/views.py</a></td>
                <td>53</td>
                <td>5</td>
                <td>0</td>
                <td class="right" data-ratio="48 53">91%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>743</td>
                <td>25</td>
                <td>0</td>
                <td class="right" data-ratio="718 743">97%</td>
            </tr>
        </tfoot>
    </table>
   
</main>

</body>
</html>

