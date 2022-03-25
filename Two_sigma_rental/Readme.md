Finding the perfect place to call your new home should be more than browsing through endless listings. 
RentHop makes apartment search smarter by using data to sort rental listings by quality. But while looking for the perfect apartment is difficult enough, 
structuring and making sense of all available real estate data programmatically is even harder. Two Sigma and RentHop, a portfolio company of Two Sigma Ventures, 
invite Kagglers to unleash their creative engines to uncover business value in this unique recruiting competition.
Two Sigma invites you to apply your talents in this recruiting competition featuring rental listing data from RentHop. 
Kagglers will predict the number of inquiries a new listing receives based on the listing’s creation date and other features. 
Doing so will help RentHop better handle fraud control, identify potential listing quality issues, 
and allow owners and agents to better understand renters’ needs and preferences.
Two Sigma has been at the forefront of applying technology and data science to financial forecasts. 
While their pioneering advances in big data, AI, and machine learning in the financial world have been pushing the industry forward, 
as with all other scientific progress, they are driven to make continual progress. 
This challenge is an opportunity for competitors to gain a sneak peek into Two Sigma's data science work outside of finance.
Submissions are evaluated using the multi-class logarithmic loss. Each listing has one true class. 

For each listing, you must submit a set of predicted probabilities (one for every listing). The formula is then,
    log loss s = -1 / N * sum(sum(y{ij} * log(p{ij}))), 1 <= i <= N, 1 <= j <= M,
where N is the number of listings in the test set, M is the number of class labels (3 classes), 
\\(log\\) is the natural logarithm, \\(y_{ij}\\) is 1 if observation \\(i\\) belongs to class \\(j\\) and 0 otherwise, 
and \\(p_{ij}\\) is the predicted probability that observation \\(i\\) belongs to class \\(j\\).

The submitted probabilities for a given listing are not required to sum to one because they are rescaled prior to being scored (each row is divided by the row sum). 
In order to avoid the extremes of the log function, predicted probabilities are replaced with \\(max(min(p, 1-10^{-15}), 10^{-15})\\).

Submission File
You must submit a csv file with the listing_id, and a probability for each class.
