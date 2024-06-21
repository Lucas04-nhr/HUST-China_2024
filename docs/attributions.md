Teams must use the standard Attributions form. To meet the attributions requirement, you must display the standard form
on your Wiki by following the instructions
here: [Project Attribution page](https://competition.igem.org/deliverables/project-attribution).

#### Bronze Medal Criterion \#2

Describe what work your team members did and what other people did for your project.

The form that has been embedded in an iframe in this page shows your team's Project Attribution form. This page must
keep the form as it is.

If you use a different website framework, make sure to embed the right URL for your team's form.

<!-- !!! LEAVE THE IFRAME CODE BELOW AS IT IS, THE ATTRIBUTION FORM OF YOUR TEAM !!! -->
<!-- !!! WILL BE DISPLAYED ON THIS PAGE. DO NOT REMOVE IT, OTHERWISE YOU RISK OF !!! -->
<!-- !!! NOT MEETING BRONZE MEDAL CRITERION #2  -->
<!-- !!! DO NOT CHANGE ITS INDENTATION !!! -->
<div class="row mt-4">
  <script type="text/javascript">
    // Listen to size change and update form height
    window.addEventListener("message", function (e) {
      if (e.origin === "https://teams.igem.org") {
        const {type, data} = JSON.parse(e.data);
        if (type === "igem-attribution-form") {
          const element = document.getElementById("igem-attribution-form");
          element.style.height = `${data + 100}px`;
        }
      }
    });
  </script>
  <iframe style='width: 100%' id="igem-attribution-form"
    src="https://teams.igem.org/wiki/5175/attributions">
  </iframe>
</div>
<!-- DO NOT REMOVE THE IFRAME CODE ABOVE -->
