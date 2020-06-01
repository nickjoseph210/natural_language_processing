# The Tree Musketeers


## Executive Summary 

Using natural language processing (NLP), we were asked to predict the programming language contained in hundreds of Github repositories based solely on the README files for that repository.  After briefly discussing the project and analyzing the data we pulled in, we formed a simple null hypothesis ('H_0') that the length of the README file would be a good indicator of the programming language used.  Provided information that Python (the language used throughout this project) was a preferred language amongst programmers becuase of its strict adherence to documentation guidelines, we assumed that longer README files pointed to program contents being written in Python as opposed to other languages like C# ('C-sharp') or Java.

After acquiring our dataset using Python and its library 'BeautifulSoup', we explored our findings to actually 'see' our findings through various visualizations made possible with Matplotlib and Seaborn.  [COMPLETE AS WE GO]


# Natural Language Processing 

Natural Language Processing (NLP) is a subfield of Artificial Intelligence (AI) concerned most specifically with human - computer interactions.  It involves assembling a body of data (a 'corpus') and reading through each aspect of it in search of patterns for prediction.  Google's latest Gmail installment provide us with a clear, although very simple, example:

People are creatures of habit, and in typing an email, Google's NLP algorithm will compare your current email's contents to countless other emails you've previously written.  In real-time, it matches patterns of your previous emails with the one you are currently writing;  previous phrases tend to follow a certain string of characters / commands you've used in the past, and as you type, it will offer time-saving suggestions that will speed up your productivity with the simple stroke of your 'Tab' key.

There are many other uses for NLP (chatbots that 'assist' you in your online purchasing endeavors, the spam filter on your personal / business email accounts, etc), and its ability to predict patterns of action / behavior is streamlining business at an ever-increasing rate.

## Project Background

Beginning 1 June 2020, our team was tasked with building an nlp (natural language processing) model to predict the programming language of a github repository based solely on the text of the README file. 

Github is an online version control platform that provides hosting services for software development.  Each repository is a publicly accessible file from which users can pull information and see the development of a program at various points in its evolution.

To those unfamiliar with the jargon-heavy vocabulary of programming, think of baking a pie for friends.  

Github is the giant cookbook filled with recipes from all over the world.  Each recipe is detailed in both its ingredients list and the step-by-step processes you need to achieve a perfectly flaky - yet tender - pie crust.

But unlike a regular cookbook, as people try these recipes, they can make adjustments to them and contribute these changes to improve the pie itself.  For instance, baking times and temperatures will be different for the cook at a low sea-level like New Orleans than it would be for the aspiring chef in the mountains of Colorado.  Each change is as detailed as possible so that anyone finding it can browse through the contents of that recipe and see exactly what it is they're looking for.  

That is the essence of GitHub: a cloud platform where people can view software development at various stages and - with the proper permissions - volunteer their contributions in an effort to improve the performance of the original product.  

Unlike previous projects involving provided sets of data, were tasked with developing our own dataset from which to lauch our efforts, implying consistent communication and collaboration throughout this project's lifecycle.  Among other things, this included individual contributions from three different origin computers into a single, readable Jupyter notebook without unknowingly rewriting / adjusting previous code.  

Team members include Shay Altshue, Ravinder Singh, and Nick Joseph.

## Scope:

Undertaking such a project involves heavy planning at its outset, for there are myriad of ways to collect data.  Once 

