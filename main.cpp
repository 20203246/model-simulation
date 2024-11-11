#include <bits/stdc++.h>
#pragma GCC optimize(1)
#pragma GCC optimize(2)
#pragma GCC optimize(3,"Ofast","inline")
using ll = int;

ll dp[760][760];
bool flag[760][760];
class Solution {
public:
    int dx[4] = {0,0,1,-1};
    int dy[4] = {1,-1,0,0};
    struct node{
        int first,second,step;
    };
    int minTimeToReach(vector<vector<int>>& a) {
        memset(flag,0,sizeof flag);
        queue<node>q;
        q.push({0,0,0});
        dp[0][0] = 0;
        int n = a.size();
        int m = a[0].size();
        flag[0][0]=true;
        while(!q.empty()) {
            node now = q.front();q.pop();
            ll origin = dp[now.first][now.second];
            for(int i = 0; i < 4; i++) {
                int xx = now.first + dx[i];
                int yy = now.second + dy[i];
                if (xx<0||xx>=n||yy<0||yy>=m) continue;
                ll dist = max((ll)a[xx][yy],origin)+(now.step&1)+1;
                if(flag[xx][yy] == 0 || dist < dp[xx][yy]) {
                    dp[xx][yy] = dist;
                    flag[xx][yy] = true;
                    q.push({xx,yy,now.step+1});
                }
            }
        }
        return dp[n-1][m-1];
    }
};

int main()
{
    a = Solution();
    
}