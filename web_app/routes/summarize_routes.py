#from flask import Blueprint, request, render_template
#
#summarize_routes = Blueprint("summarize_routes", __name__)
#
#@summarize_routes.route("/summarize", methods=["GET", "POST"])
#def summarize():
#    if request.method == "POST":
#        # Get the selected summarization option from the form
#        summary_option = request.form.get("summary_option")
#
#        # Perform summarization logic here based on the selected option
#        summarized_text = ""
#
#        if summary_option == "option1":
#            # Perform summarization using option 1
#            summarized_text = "A shorter summary."
#
#        elif summary_option == "option2":
#            # Perform summarization using option 2
#            summarized_text = "A longer summary"
#
#        # Add more options and corresponding summarization logic as needed
#
#        return render_template("summarize_result.html", summarized_text=summarized_text)
#
#    return render_template("summarize_input.html")





