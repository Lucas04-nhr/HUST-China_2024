#### Bronze Medal Criterion \#2

Describe what work your team members did and what other people did for your
project.

The form that bas been embded in an iframe in this page shows your team's
Project Attribution form. This page must keep the form as it is.

If you use a different website framework, make sure to embed the right URL for
your team's form.

---

Please see the
[Project Attribution page](https://competition.igem.org/deliverables/project-attribution)
for more information.

<!-- !!! LEAVE THE IFRAME CODE BELOW AS IT IS, THE ATTRIBUTION FORM OF YOUR TEAM !!! -->
<!-- !!! WILL BE DISPLAYED ON THIS PAGE. DO NOT REMOVE IT, OTHERWISE YOU RISK OF !!! -->
<!-- !!! NOT MEETING BRONZE MEDAL CRITERION #2  -->
<!-- !!! DO NOT CHANGE ITS INDENTATION !!! -->
<div class="row mt-4">
  <script type="text/javascript">
    // Listen to size change and update form height
    window.addEventListener("message", function (e) {
      if (e.origin === "https://attributions.igem.org") {
        const {type, data} = JSON.parse(e.data);
        if (type === "igem-attribution-form") {
          const element = document.getElementById("igem-attribution-form");
          element.style.height = `${data + 50}px`;
        }
      }
    });
  </script>
  <iframe style='width: 100%' id="igem-attribution-form"
    src="https://attributions.igem.org?team=TeamName&year=2024">
  </iframe>
</div>
<!-- DO NOT REMOVE THE IFRAME CODE ABOVE -->
