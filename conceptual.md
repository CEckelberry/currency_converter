### Conceptual Exercise

# Answer the following questions below:

- What are important differences between Python and JavaScript?
    
    Python is a multi-threaded language that is used more predominantly in backend situations whereas Javascript is single threaded and used as the front-end language for most modern websites. Python also doesn't treat 0/Undefined in the same way Javascript does and has much more verbose error handling. 
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  
  ????? dictionary["c"]
- What is a unit test?
  
  A unit test is a test of individual functions or methods.
- What is an integration test?
  
  Integration testing is when mutliple functions or pieces need to be tested in concert or together as they have shared variables\tools\functions\etc. 
- What is the role of web application framework, like Flask?

  Flask and other frameworks help organize a web application into routes while also allowing us to start a server and accept GET\POST requests. 
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  /foods/pretzel would usually be predefined or categorical as /foods/X could be any possible food. Foods?Type is probably more for search based routing. 
- How do you collect data from a URL placeholder parameter using Flask?

  request.args ??
- How do you collect data from the query string using Flask?

  request.url ??
- How do you collect data from the body of the request using Flask?

  request.args.get ??
- What is a cookie and what kinds of things are they commonly used for?

  Cookies are pieces of data that are tied to a user\computer that will be accessed whenever you visit said website. This could be search history, user preferences, etc. 
- What is the session object in Flask?

  A session is similar to a cookie, as it stores information on a user\computer that is carried over during the course of a browsers life. This can help keep track of constantly updating variables that will be referencable as long as the browser\window remain open. Not affected by refreshes. 

- What does Flask's `jsonify()` do?

  jsonify will return flask variables\data that need to be turned into the JSON format for frontend API's to consume. 