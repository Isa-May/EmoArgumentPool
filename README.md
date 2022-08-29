This is a basic django REST Api allowing to display arguments classified as 'emotional' and 'non-emotional'
by the machine learning models created in my project https://github.com/Isa-May/EmotionalArgumentationProject. An 'emotional' argument, as classified in this work, is an argument containing pathos, i.e. emotional appeal. A 'non-emotional' argument is, by contrast, not able to trigger emotions. 


Please note that the arguments are by no means selected to reflect my personal views nor are they directed towards anyone, they are simply the outcome of a research project. The sources of the data are mainly from online arguments portals and forums where people 
give their views on topics as presented in the API. - The exact sources are: 

* Toledo, A., Gretz, S., Cohen-Karlik, E., Friedman, R., Venezian, E., La- hav, D., & Slonim, N. (2019). Automatic Argument Quality Assessment– New Datasets and Methods. arXiv preprint arXiv:1909.01007.


* Swanson, R., Ecker, B., & Walker, M. (2015, September). Argument min- ing: Extracting arguments from online dialogue. In Proceedings of the 16th annual meeting of the special interest group on discourse and dialogue, pp. 217-226.


* Gretz, S., Friedman, R., Cohen-Karlik, E., Toledo, A., Lahav, D., Aharonov, R., & Slonim, N. (2020, April). A large-scale dataset for ar- gument quality ranking: Construction and analysis. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 34, No. 05, pp. 7805-7813).


* Habernal, I., & Gurevych, I. (2016, August). Which argument is more convincing? Analyzing and predicting convincingness of web arguments using bidirectional lstm. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1589-1599.

If using docker run `docker-compose up` and start the project from here:  http://127.0.0.1:8000.





