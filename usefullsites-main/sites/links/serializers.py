from rest_framework import serializers
from django.db.models import Count
import datetime
from django.db.models import Q


from .models import Tag,BunchOfLinks,CommentsModel,ReportsModel



class TagSerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model= Tag
        fields= '__all__'
    
    def to_representation(self,obj):
        print('inside Tag get')
        return_data={
            "id":obj.id,
            "name": obj.name,
            "colour_code": obj.colour_code,
            "types": obj.types,
            "description": obj.description,
            "updated_on": obj.updated_on,
            "created_on": obj.created_on

        }
        return return_data
    def create(self, obj):
        print('created')
        new_tag= Tag.objects.create(
            name=obj["name"],
            colour_code= obj["colour_code"],
            types= obj["types"],
            description= obj["description"],
                

            )
        return new_tag
    def update(self, instance,obj):
            if "name" in obj:
                instance.name = obj["name"]
            if "colour_code" in obj:
                instance.colour_code = obj["colour_code"]
            if "types" in obj:
                instance.types = obj["types"]
            if "description" in obj:
                instance.description = obj["description"]
            
            instance.save()
            return instance


class LinkSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    brandlogo = serializers.URLField(allow_null=True)
    url = serializers.URLField(allow_null=True)
    # taglist = serializers.ListField(child=serializers.CharField(allow_null=True))
    upvote=serializers.IntegerField(allow_null=True)
    downvote=serializers.IntegerField(allow_null=True)
    followers=serializers.IntegerField(allow_null=True)


    class Meta:
        model=BunchOfLinks
        fields='__all__'

    def to_representation(self, instance):
        print('am inside representation')
        print(instance)
        comments=CommentsModel.objects.filter(bunch_of_links=instance.id)
        # print(comments)


        commentsdata=commentsrepresentation(comments,many=True)
        reports=ReportsModel.objects.filter(bunch_of_links=instance.id)
        reportsdata=ReportsSerializer(reports,many=True)
        return_links={
            "id":instance.id,
            "name":instance.name,
            "description":instance.description,
            "brandlogo": instance.brandlogo,
            "url":instance.url,
            "upvote":instance.upvote,
            "downvote":instance.downvote,
            "bookmark":instance.bookmark,
            "followers":instance.followers,
            "comments":commentsdata.data,
            "reports":reportsdata.data,
            "created_on":instance.created_on,
            "updated_on":instance.updated_on
        }
        return return_links
        # return super().to_representation(return_links)

    def create(self, validated_data,):
        print('inside serializer')
        2# update=get_object_or_404(CommentsModel,pk=id)

        bunch_links=BunchOfLinks.objects.create(
            name=validated_data["name"],
            brandlogo=validated_data["brandlogo"],
            url=validated_data["url"],
            description=validated_data["description"],
            # taglist=validated_data["taglist"],
            upvote=validated_data["upvote"],
            downvote=validated_data["downvote"],
            bookmark=validated_data["bookmark"],
            followers=validated_data["followers"]

        )
        # if "upvote" in CommentsModel==True:
        #     bunch_links.upvote+=1


            
            

        return bunch_links
        # return super().create(bunch_links)
    def update(self, instance,obj):
            if "name" in obj:
                instance.name = obj["name"]
            if "brandlogo" in obj:
                instance.brandlogo = obj["brandlogo"]
            if "url" in obj:
                instance.url = obj["url"]
            if "description" in obj:
                instance.description = obj["description"]
            # if "taglist" in obj:
            #     instance.description = obj["taglist"]
            if "upvote" in obj:
                instance.upvote = obj["upvote"]
            if "downvote" in obj:
                instance.downvote = obj["downvote"]
            if "bookmark" in obj:
                instance.description = obj["bookmark"]
            
            instance.save()
            return instance


class CommentSerializer(serializers.ModelSerializer):
    comments = serializers.CharField(allow_null=True)
    upvote=serializers.BooleanField(allow_null=True)
    downvote=serializers.BooleanField(allow_null=True)
    bunch_of_links = serializers.CharField(allow_null=True)
    followers=serializers.BooleanField(allow_null=True)

    class Meta:
        model=CommentsModel
        fields='__all__'


    def to_representation(self, instance):

        bunch_of_links = None
        if instance.bunch_of_links is not None :
            bunch_of_links = instance.bunch_of_links.id
        followers=False
        if instance.followers is True:
            followers=instance.followers
        print("inside get section comments")
        # votevar=BunchOfLinks.objects.get(id=instance.id)
        # print(votevar)

        return_comments={
            "id":instance.id,
            "comments": instance.comments,
            "upvote": instance.upvote,
            "downvote": instance.downvote,
            "bunch_of_links":bunch_of_links,
            "followers":instance.followers,
            "created_on":instance.created_on,
            "updated_on":instance.updated_on
        

        }
        print(instance.upvote)
        print(bunch_of_links)
        return return_comments


    def create(self, validated_data):
        print('inside comment section create')

        commentscreate= CommentsModel.objects.create(
            comments=validated_data["comments"],
            upvote=validated_data["upvote"],
            downvote=validated_data["downvote"],
            bunch_of_links=BunchOfLinks.objects.get(id=validated_data["bunch_of_links"]),     #for foreign keys
            # followers=BunchOfLinks.objects.get(id=validated_data["followers"])
            # followers=validated_data["followers"]

        )

            
        votevar=BunchOfLinks.objects.get(id=validated_data["bunch_of_links"])
        followvar=BunchOfLinks.objects.get(id=validated_data["followers"])
        print('followers id',validated_data["followers"])
        print("llinks id", validated_data["bunch_of_links"])

        # if "followers" in validated_data:
        #     if validated_data["followers"] is True:
        #         print("follower increased")
        #         followvar.followers+=1
        if "upvote" in validated_data:
            if validated_data["upvote"] is True:
                print("Its true")
                votevar.upvote+=1
        if "downvote" in validated_data:
            if validated_data["downvote"] is True:
                print("Its true")
                votevar.downvote+=1

        # if commentscreate.upvote==True:
            # print("inside if")
            # upvotevar.upvote+=1
        votevar.save()

        # commentscreate.bunch_of_links.upvote+=1
        # commentscreate.save()
        print(votevar.upvote)
        print("downvote is", votevar.downvote)

        # if commentscreate.upvote== True:
        #     BunchOfLinks.upvote=+1

        return commentscreate

    def update(self, instance,obj):
        print('inside update---serializer')
        print(instance.comments)

        if "comments" in obj:
            instance.comments = obj["comments"]


            # instance.upvote = obj["upvote"]
            


        if "bunch_of_links" in obj:
            instance.bunch_of_links=BunchOfLinks.objects.get(id=obj["bunch_of_links"])     #for foreign keys

            # print(instance.bunch_of_links)
        if "followers" in obj:
            instance.followers = obj["followers"]

        if "downvote" in obj:
            instance.downvote = obj["downvote"]
         


        bunch_of_links=BunchOfLinks.objects.get(id=obj["bunch_of_links"])    
    
        if "upvote" in obj:
            print(instance.upvote)
            print(obj["upvote"])
            if (instance.upvote) != obj["upvote"]:
                if obj["upvote"] is True:
                    print("1111")
                    bunch_of_links.upvote=bunch_of_links.upvote+1
                    print(bunch_of_links)
                    print("inside if")
                else:
                    print("else part")
                    bunch_of_links.upvote-=1
                instance.upvote=obj["upvote"]
        
        
        instance.save()
        bunch_of_links.save()
        print(instance.bunch_of_links)
        return instance


class commentsrepresentation(serializers.ModelSerializer):
    comments = serializers.CharField(allow_null=True)
    bunch_of_links = serializers.CharField(allow_null=True)
    class Meta:
        model=CommentsModel
        fields='__all__'
    def to_representation(self, instance):
        # comments=CommentsModel.objects.filter(bunch_of_links=instance.id)
        # commentsdata=CommentSerializer(comments,many=True)



        bunch_of_links = None
        if instance.bunch_of_links is not None:
            bunch_of_links = instance.bunch_of_links.id

        print("inside get section comments")

        print(bunch_of_links)
        return_comments={
            "comments": instance.comments,
            # "bunch_of_links":bunch_of_links,

        }
        return return_comments

class HotDashboardserializer(serializers.Serializer):
    hot=serializers.SerializerMethodField()
    # toplinks = serializers.SerializerMethodField()
    links_added_last7_days=serializers.SerializerMethodField()
    highestupvotes=serializers.SerializerMethodField()
    risingcomments=serializers.SerializerMethodField()
    print("12345",hot)
    class Meta:
        model=CommentsModel
        fields={
            "hot",
            "links_added_last7_days",
            "highestupvotes",
            "risingcomments"
        }
    

    def get_hot(self,obj):

        print('hot serializer')

        lastdate = datetime.datetime.now() - datetime.timedelta(30)
        print(lastdate)

# count=lastdate
 
        toplinks = CommentsModel.objects.filter(updated_on__gte=lastdate.date(),upvote=True).values('bunch_of_links').annotate(count=Count('bunch_of_links')).order_by('-count')
        # toplinks=toplinks.values('bunch_of_links')
        # # .order_by("-updated_on")
        # .values('downvote'))  

        print(toplinks)

        # comment_serializer=CommentSerializer(toplinks,many=True)
        # upvotecount=(CommentsModel.objects.filter(upvote=True)
        # .values("upvote")
        # .annotate(count=Count('upvote')))
        # .order_by('-count'))



        print('11111')
        return toplinks
    def get_links_added_last7_days(self, obj):
        lastdate = datetime.datetime.now() - datetime.timedelta(7)
        links_added_last7_days = (BunchOfLinks.objects.filter(updated_on__gte = lastdate.date())).values('url')
        return links_added_last7_days
    
    def get_highestupvotes(self,obj):
        highest = CommentsModel.objects.filter(upvote=True).exclude(bunch_of_links__isnull=True).values('bunch_of_links').annotate(count=Count('upvote')).order_by("-count")
        # .values("upvote")
        # .annotate(count=Count('upvote'))
        # .count())
        return highest
    def get_risingcomments(self,obj):
        lastdate = datetime.datetime.now() - datetime.timedelta(30)

        rising30 = (CommentsModel.objects.filter(updated_on__gte=lastdate).exclude(bunch_of_links__isnull=True)
        .values("bunch_of_links").annotate(count=Count("comments")).order_by('-count')
        
        )

        
        return rising30




class ReportsSerializer(serializers.ModelSerializer):
    print("1234")
    bunch_of_links = serializers.CharField(allow_null=True)
    report = serializers.CharField(allow_null=True)

    class Meta:
        model=ReportsModel
        fields='__all__'

    def to_representation(self, instance):

        bunch_of_links = None
        if instance.bunch_of_links is not None:
            bunch_of_links = instance.bunch_of_links.id
        return_report={
            # "id":instance.id,
            "report": instance.report,
            # "bunch_of_links":bunch_of_links
        }
        return return_report

    def create(self, validated_data):
        print("inside report section")
        reportcreate=ReportsModel.objects.create(
            report=validated_data["report"],
            bunch_of_links=BunchOfLinks.objects.get(id=validated_data["bunch_of_links"])     #for foreign keys
        )
        return reportcreate