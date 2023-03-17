#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


import replicate
import os
os.environ["REPLICATE_API_TOKEN"] = "ce3e7671659d7f117cfe93b662c2f88052b12515"
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")


# In[ ]:


app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("txt")
        inputs = {"prompt":q}
        out = version.predict(**inputs)
        return(render_template("index.html", result = out[0]))
    else:
        return(render_template("index.html", result = "waiting"))
if __name__ == "__main__":
    app.run()


# In[ ]:




