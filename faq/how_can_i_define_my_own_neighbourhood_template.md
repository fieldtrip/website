---
title: How can I define my own neighbourhood templates or updating an already existing template?
tags: [faq, statistics, cluster]
---

# How can I define my own neighbourhood templates or updating an already existing template?

Currently, each entry of the neighbour-structure needs to have two fields: 'label' and 'neighblabel'. cfg.neighbours must be a struct-array, with each entry having these two fields. You can then define the structure as follow

	  cfg.neighbours = struct;
	  cfg.neighbours(1).label = 'Fp1';
	  cfg.neighbours(1).neighblabel = {'Fpz'; 'AFz'};

Similarly, you can load a template and then change the neighbour definition. Note, that you should verify your definition using **[ft_neighbourplot](/reference/ft_neighbourplot)**.
