```text

  _________              __    _________ .__             __                      
 /   _____/ ____________/  |_  \_   ___ \|  |   ____    |__|__ _________   ____  
 \_____  \ /  _ \_  __ \   __\ /    \  \/|  |  /  _ \   |  |  |  \_  __ \_/ __ \ 
 /        (  <_> )  | \/|  |   \     \___|  |_(  <_> )  |  |  |  /|  | \/\  ___/ 
/_______  /\____/|__|   |__|    \______  /____/\____/\__|  |____/ |__|    \___  >
        \/                             \/           \______|                  \/ 

```

# Sort Clojure Namespaces
A simple python script to sort require namespaces in alphabetic order of clojure source file.

# How to run 
```bash
python sort.py /path/to/clojure/directories
```

* Before sorting
```clojure
(ns example
  (:require [clj-time.core :as t]
            [monger.collection :as mc]
            [monger.operators :refer :all]
            [service.config :refer [env]]
            [util :as dbcore]
            [banana.config :refer [env]]
            [clj-time.config :refer [env]]
            [monger.config :refer [env]]
            [apple.config :refer [env]]
            [service.config :refer [env]]
            [apple.util.common :as common]))


(defn name
  "docstring"
  [arglist]
  )
  
(defn name2
  "docstring"
  [arglist]
  )
```

* After sorting
```clojure
(ns example
  (:require [apple.config :refer [env]]
            [apple.util.common :as common]
            [banana.config :refer [env]]
            [clj-time.config :refer [env]]
            [clj-time.core :as t]
            [monger.collection :as mc]
            [monger.config :refer [env]]
            [monger.operators :refer :all]
            [service.config :refer [env]]
            [service.config :refer [env]]
            [util :as dbcore]))


(defn name
  "docstring"
  [arglist]
  )

(defn name2
  "docstring"
  [arglist]
  )
```